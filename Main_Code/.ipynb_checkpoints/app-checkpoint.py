from flask import Flask, render_template, jsonify, request
import sqlite3
import pandas as pd
import folium
from folium.plugins import HeatMap
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

#DATABASE CONNECTION
def get_db_connection():
    conn = sqlite3.connect('accidents.db')
    conn.row_factory = sqlite3.Row
    return conn

# ROUTES

@app.route('/', methods=['GET', 'POST'])
def index():
    visualization_html = ''

    if request.method == 'POST':
        selected_viz = request.form.get('viz')

        if selected_viz == 'histogram':
            conn = get_db_connection()
            df = pd.read_sql('SELECT no__of_vehicles FROM accident_details', conn)
            conn.close()

            plt.figure(figsize=(10, 6))
            sns.histplot(df['no__of_vehicles'], bins=10, kde=True)
            plt.title("Number of Vehicles Involved in Accidents")

            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode()
            plt.close()

            visualization_html = f'<img src="data:image/png;base64,{plot_url}"/>'

        elif selected_viz == 'boxplot':
            conn = get_db_connection()
            df = pd.read_sql('SELECT severity, road_surface FROM traffic_data', conn)
            conn.close()

            plt.figure(figsize=(10, 5))
            sns.boxplot(data=df, x='road_surface', y='severity')
            plt.xticks(rotation=45, ha='right')  
            plt.title("Accident Severity by Road Surface")
            plt.tight_layout(pad=2)

            img = io.BytesIO()
            plt.savefig(img, format='png', bbox_inches='tight')
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode()
            plt.close()

            visualization_html = f'<img src="data:image/png;base64,{plot_url}"/>'

        elif selected_viz == 'heatmap':
            conn = get_db_connection()
            df = pd.read_sql('SELECT latitude, longitude FROM accidents_data', conn)
            conn.close()

            m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=12)
            heat_data = [[row['latitude'], row['longitude']] for _, row in df.iterrows()]
            HeatMap(heat_data).add_to(m)

            visualization_html = m.get_root().render()

    return render_template('index.html', visualization=visualization_html)

# API Line Chart Data
@app.route('/api/linechart')
def api_line_chart():
    severity = request.args.get('severity', 'all')

    conn = get_db_connection()

    if severity == 'all':
        query = '''
            SELECT date, COUNT(*) as accident_count
            FROM accidents_data
            GROUP BY date
        '''
        df = pd.read_sql(query, conn)

    elif severity == 'blank':
        query = '''
            SELECT date, COUNT(*) as accident_count
            FROM accidents_data
            WHERE severity IS NULL OR TRIM(severity) = ''
            GROUP BY date
        '''
        df = pd.read_sql(query, conn)

    else:
        query = '''
            SELECT date, COUNT(*) as accident_count
            FROM accidents_data
            WHERE severity = ?
            GROUP BY date
        '''
        df = pd.read_sql(query, conn, params=(severity,))

    conn.close()
    return jsonify(df.to_dict(orient='records'))

# Heatmap visual route
@app.route('/heatmap')
def heatmap():
    conn = get_db_connection()
    df = pd.read_sql('SELECT latitude, longitude FROM accidents_data', conn)
    conn.close()

    m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=12)
    heat_data = [[row['latitude'], row['longitude']] for _, row in df.iterrows()]
    HeatMap(heat_data).add_to(m)
    m.save('templates/heatmap.html')

    return render_template('heatmap.html')

# APP ENTRY POINT
if __name__ == '__main__':
    app.run(debug=True)
