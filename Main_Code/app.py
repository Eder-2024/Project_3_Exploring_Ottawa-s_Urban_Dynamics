from flask import Flask, render_template, request, jsonify
import sqlite3
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64
import folium
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster
from matplotlib import cm


app = Flask(__name__)

# connect to the SQlite database and create a connection object
def get_db_connection():
    conn = sqlite3.connect('accidents.db')
    conn.row_factory = sqlite3.Row
    return conn

# Flask route for the homepage, accepts both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index():
    visualization_html = ''
    stats_output = ''

    # --- Calculate Injury Totals (always) ---
    conn = get_db_connection()
    injury_query = '''
        SELECT severity, COUNT(*) as count
        FROM accidents_data
        WHERE severity IS NOT NULL
        GROUP BY severity
    '''
    #SQL query: count the number of accidents grouped by severity
    #connect to the database and execute the query
    df_injuries = pd.read_sql_query(injury_query, conn)
    
    # Get all accident coordinates where both latitude and longitude are present
    map_df = pd.read_sql('SELECT latitude, longitude FROM accidents_data WHERE latitude IS NOT NULL AND longitude IS NOT NULL', conn)
    conn.close()

    # Check if the DataFrame is empty before creating the map
    # Create a map centered around the mean Latitude and Longitude of the accident data  
    if not map_df.empty:
        map_center = [map_df['latitude'].mean(), map_df['longitude'].mean()]
        traffic_map = folium.Map(location=map_center, zoom_start=12, tiles='openStreetmap')
    
    # fetch severity from the DB h
        conn = get_db_connection()
        s_df = pd.read_sql_query("SELECT date, latitude, longitude, severity FROM accidents_data WHERE latitude IS NOT NULL AND longitude IS NOT NULL", conn)
        conn.close()
        
        # Generate a list of unique severity values, excluding null entries and case-insensitive 'none' 
        severities = [s for s in s_df['severity'].unique() if pd.notna(s) and s.lower() != 'none']

    # # Create a Folium map centered on average accident location with a specific tile style
        for severity in severities:
            fg = folium.FeatureGroup(name=f"Severity: {severity}")
            cluster = MarkerCluster()
            for _, row in s_df[s_df['severity'] == severity].iterrows():
                folium.Marker(
                    location=[row['latitude'], row['longitude']],
                    popup=f"Date: {row['date']}<br>Severity: {row['severity']}",
                    icon=folium.Icon(
                        icon = ("times-circle" if severity == "04 - Fatal"
                            else "exclamation-triangle" if severity == "03 - Major"
                            else "exclamation-circle" if severity == "02 - Minor"
                            else "info-circle"),# Minimal severity
                        prefix = "fa",  
                        color = ("darkred" if severity == "04 - Fatal"
                            else "red" if severity == "03 - Major"
                            else "orange" if severity == "02 - Minor"
                            else "green"), # Minimal severity
                        icon_color="white"
                        )
                ).add_to(cluster)
            fg.add_child(cluster)
            traffic_map.add_child(fg)
    
    # Add layer control to toggle severity layers
        folium.LayerControl().add_to(traffic_map)
    
     #Render the map as HTML 
        map_html = traffic_map._repr_html_()
    else:
        map_html = "<p>No accident data with coordinates found.</p>"

    # Initialize dictionary with all keys
    injury_totals = {
        'Minimal': 0,
        'Minor': 0,
        'Major': 0,
        'Fatal': 0
    }

    for _, row in df_injuries.iterrows():
        sev = row['severity'].strip() if row['severity'] else 'Unknown'
        if sev.startswith('01'):
            injury_totals['Minimal'] += row['count']
        elif sev.startswith('02'):
            injury_totals['Minor'] += row['count']
        elif sev.startswith('03'):
            injury_totals['Major'] += row['count']
        elif sev.startswith('04'):
            injury_totals['Fatal'] += row['count']
        else:
            continue

    # --- Handle Form POST ---
    if request.method == 'POST':
        selected_viz = request.form.get('viz')
        selected_analysis = request.form.get('analysis')

        if selected_viz == 'histogram': 
            conn = get_db_connection() 
            df = pd.read_sql('SELECT no__of_vehicles FROM accident_details', conn) 
            conn.close() 
            plt.figure(figsize=(10, 6)) 
            sns.histplot(df['no__of_vehicles'], bins=10, kde=True) 
            plt.title("Number of Vehicles Involved in Accidents")

        elif selected_viz == 'light_conditions':
            conn = get_db_connection()
            query = '''SELECT light, COUNT(*) as accident_count FROM accident_details
                    GROUP BY light ORDER BY accident_count DESC;'''
            df = pd.read_sql_query(query, conn)
            conn.close()
            plt.figure(figsize=(8, 8))

            # Generate colors using the 'viridis' colormap
            
            cmap = cm.get_cmap('viridis')
            colors = [cmap(i / len(df)) for i in range(len(df))]

            plt.pie(df['accident_count'], labels=df['light'], autopct='%1.1f%%', startangle=140, colors=colors)
            plt.title('Number of Accidents by Light Conditions')
            plt.tight_layout()

        elif selected_viz == 'environment_conditions':
            conn = get_db_connection()
            query = '''SELECT environment_condition, COUNT(*) as accident_count
                       FROM accident_details GROUP BY environment_condition ORDER BY accident_count DESC;'''
            df = pd.read_sql_query(query, conn)
            conn.close()
            plt.figure(figsize=(10, 6))
            plt.bar(df['environment_condition'], df['accident_count'], color='lightblue')
            plt.title('Accidents by Environmental Conditions')
            plt.xticks(rotation=45)
            plt.tight_layout()

        elif selected_viz == 'severity_weather':
            conn = get_db_connection()
            query = '''SELECT severity, tavg, prcp FROM accidents_data
                       JOIN weather_data ON accidents_data.date = weather_data.date;'''
            df = pd.read_sql_query(query, conn)
            conn.close()
            df = df.dropna()
            plt.figure(figsize=(10, 6))
            plt.scatter(df['tavg'], df['severity'], alpha=0.6, c=df['prcp'], cmap='viridis')
            plt.colorbar(label='Precipitation')
            plt.title('Severity vs Average Temperature')
            plt.xlabel('Temperature (°C)')
            plt.ylabel('Severity')
            plt.tight_layout()

        #Demilade code 
        elif selected_viz == 'hourly_accidents':
            conn = get_db_connection()
            query = """SELECT * FROM accident_details"""
            df = pd.read_sql_query(query, conn)
            conn.close()

            # Convert 'accident_time' to datetime and extract the hour of the day
            df['accident_time'] = pd.to_datetime(df['accident_time'], format='%I:%M %p', errors='coerce')
            df['hour_of_day'] = df['accident_time'].dt.hour

            # Plot number of accidents by hour
            plt.figure(figsize=(10, 6))
            sns.countplot(x='hour_of_day', data=df, hue='hour_of_day', palette='viridis', legend=False)
            plt.title('Number of Accidents by Hour of the Day')
            plt.xlabel('Hour of the Day')
            plt.ylabel('Accident Count')
            plt.xticks(range(0, 24))
            plt.tight_layout()

        elif selected_viz == 'accidents_by_location':
            conn = get_db_connection()
            query = """SELECT * FROM accident_details;"""
            df = pd.read_sql_query(query, conn)
            conn.close()

            total = len(df)
            plt.figure(figsize=(10, 6))
            ax = sns.countplot(x='accident_location', data=df, palette='viridis')
            plt.title('Percentage of Accidents by Location')
            plt.xlabel('Accident Location')
            plt.ylabel('Percentage of Total Accidents (%)')

            # Add percentage labels
            for p in ax.patches:
                count = p.get_height()
                percent = (count / total) * 100
                ax.annotate(f'{percent:.1f}%', 
                            (p.get_x() + p.get_width() / 2., count),
                            ha='center', va='bottom', fontsize=10, color='black', xytext=(0, 3), textcoords='offset points')

            # Set y-ticks as percentage
            yticks = ax.get_yticks()
            ax.set_yticklabels([f'{(y / total) * 100:.0f}%' for y in yticks])
            handles, labels = ax.get_legend_handles_labels()
            if not handles:
                unique_locations = df['accident_location'].unique()
                handles = [plt.Rectangle((0,0),1,1, color=color) for color in sns.color_palette('viridis', len(unique_locations))]
                labels = unique_locations

            plt.legend(handles, labels, title='Accident Location', bbox_to_anchor=(1.05, 1), loc='upper left')


            plt.xticks(rotation=15, ha='right')
            plt.tight_layout()

        elif selected_viz == 'traffic_control':
            conn = get_db_connection()
            query = """SELECT * FROM accident_details;"""
            df = pd.read_sql_query(query, conn)
            conn.close()

            total = len(df)
            plt.figure(figsize=(10, 6))
            ax = sns.countplot(x='traffic_control', data=df, palette='viridis')
            plt.title('Percentage of Accidents by Traffic Control')
            plt.xlabel('Traffic Control')
            plt.ylabel('Percentage of Total Accidents (%)')

            # Add percentage labels
            for p in ax.patches:
                count = p.get_height()
                percent = (count / total) * 100
                ax.annotate(f'{percent:.1f}%',
                            (p.get_x() + p.get_width() / 2., count),
                            ha='center', va='bottom', fontsize=10, color='black', xytext=(0, 3), textcoords='offset points')

            # Set y-ticks as percentage
            yticks = ax.get_yticks()
            ax.set_yticklabels([f'{(y / total) * 100:.0f}%' for y in yticks])

            # Clean and consistent x-axis labels
            ax.set_xticklabels(ax.get_xticklabels(), rotation=20, ha='right')

            # Create a legend with color patches matching each category
            unique_traffic = df['traffic_control'].unique()
            colors = sns.color_palette('viridis', len(unique_traffic))
            handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in colors]
            plt.legend(handles, unique_traffic, title='Traffic Control', bbox_to_anchor=(1.05, 1), loc='upper left')


            plt.tight_layout()

        elif selected_viz == 'Heatmap_of_Accidents':
            conn = get_db_connection()
            query = """SELECT * FROM accident_details;"""
            df = pd.read_sql_query(query, conn)
            # Group and count accidents
            grouped = df.groupby(['accident_location', 'traffic_control']).size().reset_index(name='accident_count')

            # Pivot to matrix format
            heatmap_data = grouped.pivot(index='accident_location', columns='traffic_control', values='accident_count').fillna(0)

            # Plot heatmap with coolwarm color palette
            plt.figure(figsize=(12, 8))
            sns.heatmap(heatmap_data, annot=True, fmt='.0f', cmap='coolwarm', linewidths=0.5, cbar_kws={'label': 'Number of Accidents'})

            # Labels and titles
            plt.title('Heatmap of Accidents by Location and Traffic Control', fontsize=14)
            plt.xlabel('Traffic Control', fontsize=12)
            plt.ylabel('Accident Location', fontsize=12)
            plt.xticks(rotation=30, ha='right')
            plt.yticks(rotation=0)
            plt.tight_layout()

        elif selected_viz == 'Daily_Accidents_by_Weather':
            conn = get_db_connection()
            query = """SELECT * FROM accident_details"""
            df = pd.read_sql_query(query, conn)
            conn.close()

            # Force conversion of collision_time to datetime format
            df['accident_date'] = pd.to_datetime(df['accident_date'], errors='coerce')
            # Drop rows where datetime conversion failed (optional but helps)
            df = df.dropna(subset=['accident_date'])
            # Now extract date again for grouping
            df['date'] = df['accident_date'].dt.date
            daily_weather_collisions = df.groupby(['date', 'environment_condition']).size().unstack().fillna(0)
            # Plot the trend over time
            plt.figure(figsize=(12, 6))
            daily_weather_collisions.plot(kind='line', figsize=(12, 6), marker='o')
            plt.title('Daily Accidents by Weather Condition in 2020')
            plt.xlabel('Date')
            plt.ylabel('Number of Accidents')
            plt.xticks(rotation=45)
            plt.legend(title='Weather Type', bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.tight_layout()

        elif selected_viz == 'Number_of_Accidents_by_Day':
            conn = get_db_connection()
            query = """SELECT * FROM accident_details"""
            df = pd.read_sql_query(query, conn)
            conn.close()

            # Ensure 'accident_date' is in datetime format
            df['accident_date'] = pd.to_datetime(df['accident_date'], errors='coerce')
            # Drop rows where date parsing failed
            df = df.dropna(subset=['accident_date'])
            # Extract day of the week
            df['day_of_week'] = df['accident_date'].dt.day_name()
            # Optional: Create an ordered category for plotting (Monday to Sunday)
            days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=days_order, ordered=True)
            # Count the number of accidents per day
            day_counts = df['day_of_week'].value_counts().sort_index()
            # Plot
            plt.figure(figsize=(10, 6))
            sns.barplot(x=day_counts.index, y=day_counts.values, palette='viridis')
            plt.title('Number of Accidents by Day of the Week in 2020')
            plt.xlabel('Day of the Week')
            plt.ylabel('Number of Accidents')
            plt.xticks(rotation=45)
            plt.tight_layout()

        

        if selected_viz and selected_viz != 'heatmap':
            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode()
            plt.close()
            visualization_html = f'<img src="data:image/png;base64,{plot_url}"/>'

        elif selected_viz == 'heatmap':
            conn = get_db_connection()
            df = pd.read_sql('SELECT latitude, longitude FROM accidents_data', conn)
            conn.close()
            m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=12)
            HeatMap(df[['latitude', 'longitude']].values.tolist()).add_to(m)
            visualization_html = m.get_root().render()
        
        

        # ---- STATISTICAL SECTION ----
        if selected_analysis == 'snow_test':
            conn = get_db_connection()
            snow = pd.read_sql('''SELECT ad.no__of_vehicles FROM accident_details ad
                              JOIN weather_data wd ON ad.accident_date = wd.date WHERE wd.snow > 0''', conn)
            no_snow = pd.read_sql('''SELECT ad.no__of_vehicles FROM accident_details ad
                                 JOIN weather_data wd ON ad.accident_date = wd.date WHERE wd.snow = 0''', conn)
            conn.close()
            t_stat, p_val = stats.ttest_ind(snow['no__of_vehicles'], no_snow['no__of_vehicles'])

            stats_output = {
            'message': f"Snow vs No Snow → T: {t_stat:.2f}, P: {p_val:.5f}",
            't_stat': t_stat,
            'p_val': p_val
        }


        elif selected_analysis == 'precip_test':
            conn = get_db_connection()
            wet = pd.read_sql('''SELECT ad.no__of_vehicles FROM accident_details ad
                                 JOIN weather_data wd ON ad.accident_date = wd.date WHERE wd.prcp > 0''', conn)
            dry = pd.read_sql('''SELECT ad.no__of_vehicles FROM accident_details ad
                                 JOIN weather_data wd ON ad.accident_date = wd.date WHERE wd.prcp = 0''', conn)
            conn.close()
            t_stat, p_val = stats.ttest_ind(wet['no__of_vehicles'], dry['no__of_vehicles'])
            stats_output = f"Precipitation vs No Precipitation → T: {t_stat:.2f}, P: {p_val:.5f}"

        elif selected_analysis == 'correlation_analysis':
            conn = get_db_connection()
            df = pd.read_sql('''SELECT wd.tavg, wd.wspd, wd.snow, wd.prcp, ad.no__of_fatal
                                FROM accident_details ad JOIN weather_data wd ON ad.accident_date = wd.date''', conn)
            conn.close()
            corr = df.corr(numeric_only=True)
            plt.figure(figsize=(8, 6))
            sns.heatmap(corr, annot=True, cmap='coolwarm')
            plt.title('Correlation: Weather vs Fatalities')
            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode()
            plt.close()
            visualization_html = f'<img src="data:image/png;base64,{plot_url}"/>'

        elif selected_analysis == 'regression_analysis':
            conn = get_db_connection()
            df = pd.read_sql('''SELECT wd.tavg, wd.wspd, wd.snow, wd.prcp, ad.no__of_fatal
                                FROM accident_details ad JOIN weather_data wd ON ad.accident_date = wd.date
                                WHERE wd.tavg IS NOT NULL''', conn)
            conn.close()
            df.dropna(inplace=True)
            X = sm.add_constant(df[['tavg', 'wspd', 'snow', 'prcp']])
            y = df['no__of_fatal']
            model = sm.OLS(y, X).fit()
            stats_output = model.summary().as_text()

    return render_template(
        'index.html',
        visualization=visualization_html,
        stats_output=stats_output,
        injury_totals=injury_totals,
        map_html=map_html  
    )
@app.route('/api/linechart')
def api_line_chart():
    severity = request.args.get('severity', 'all')
    conn = get_db_connection()
    if severity == 'all':
        df = pd.read_sql('SELECT date, COUNT(*) as accident_count FROM accidents_data GROUP BY date', conn)
    elif severity == 'blank':
        df = pd.read_sql('SELECT date, COUNT(*) as accident_count FROM accidents_data WHERE severity IS NULL OR TRIM(severity) = "" GROUP BY date', conn)
    else:
        df = pd.read_sql('SELECT date, COUNT(*) as accident_count FROM accidents_data WHERE severity = ? GROUP BY date', conn, params=(severity,))
    conn.close()
    return jsonify(df.to_dict(orient='records'))

@app.route('/heatmap')
def heatmap():
    conn = get_db_connection()
    df = pd.read_sql('SELECT latitude, longitude FROM accidents_data', conn)
    conn.close()
    m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=11)
    HeatMap(df[['latitude', 'longitude']].values.tolist()).add_to(m)
    return m.get_root().render()

@app.route('/map', methods=['GET'])
def map_view():
    # Generate the map
    conn = get_db_connection()
    query = """
    SELECT date, latitude, longitude, severity
    FROM accidents_data
    WHERE latitude IS NOT NULL AND longitude IS NOT NULL
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    map_center = [df['latitude'].mean(), df['longitude'].mean()]
    traffic_map = folium.Map(location=map_center, zoom_start=12, tiles='CartoDB positron')
    severities = df['severity'].unique()

    for severity in severities:
        fg = folium.FeatureGroup(name=f"Severity: {severity}")
        cluster = MarkerCluster()
        for _, row in df[df['severity'] == severity].iterrows():
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=f"Date: {row['date']}<br>Severity: {row['severity']}",
                icon=folium.Icon(
                                color="red" if severity.lower() == "severe"
                                            else "orange" if severity.lower() == "moderate"
                                            else "green"  
)
            ).add_to(cluster)
        fg.add_child(cluster)
        traffic_map.add_child(fg)

    folium.LayerControl().add_to(traffic_map)
    map_html = traffic_map._repr_html_()


    return render_template('map.html', map_html=map_html)

@app.route('/api/top_dates')
def api_top_dates():
    conn = get_db_connection()
    query = '''
        SELECT accident_date, COUNT(*) as accident_count 
        FROM accident_details 
        GROUP BY accident_date 
        ORDER BY accident_count DESC 
        LIMIT 10;
    '''
    df = pd.read_sql_query(query, conn)
    conn.close()

    # Convert to datetime safely
    df['accident_date'] = pd.to_datetime(df['accident_date'])

    # Format the output
    result = [{
        'date': row['accident_date'].strftime('%b %d, %Y'),
        'count': row['accident_count']
    } for _, row in df.iterrows()]

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)