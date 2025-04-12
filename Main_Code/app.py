from flask import Flask, render_template, jsonify, request
import sqlite3
import pandas as pd
import plotly.express as px
import folium
from folium.plugins import HeatMap
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# === DATABASE CONNECTION ===
def get_db_connection():
    conn = sqlite3.connect('accidents.db')
    conn.row_factory = sqlite3.Row
    return conn

# === ROUTES ===

@app.route('/')
def index():
    return render_template('index.html')

# --- API: Line Chart Data ---

@app.route('/api/linechart')
def api_line_chart():
    severity = request.args.get('severity', 'all')  # Get severity filter from URL

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

# --- API: Box Plot Data ---
@app.route('/api/boxplot')
def api_box_plot():
    conn = get_db_connection()
    df = pd.read_sql('SELECT severity, road_surface FROM traffic_data', conn)
    conn.close()
    return jsonify(df.to_dict(orient='records'))

# --- API: Histogram Data ---
@app.route('/api/histogram')
def api_histogram():
    conn = get_db_connection()
    df = pd.read_sql('SELECT no__of_vehicles FROM accident_details', conn)
    conn.close()
    return jsonify(df.to_dict(orient='records'))

# === VISUAL ROUTES ===

# --- LINE CHART (HTML Page) ---

@app.route('/linechart')
def line_chart():
    conn = get_db_connection()
    df = pd.read_sql('SELECT date, COUNT(*) AS accident_count FROM accidents_data GROUP BY date', conn)
    conn.close()
    fig = px.line(df, x='date', y='accident_count', title='Accident Trends Over Time')
    return fig.to_html()

# --- HEATMAP ---
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

# --- BOXPLOT (Rendered Chart) ---
@app.route('/boxplot')
def boxplot():
    conn = get_db_connection()
    # Fetching data from the correct column 'road_surface' in traffic_data table
    df = pd.read_sql('SELECT severity, road_surface FROM traffic_data', conn)
    conn.close()

    # Create the boxplot
    plt.figure(figsize=(20, 10))
    sns.boxplot(data=df, x='road_surface', y='severity')  # Use 'road_surface' instead of 'road_surface_condition'
    plt.title("Accident Severity by Road Surface")

    # Saving the plot to a byte stream to render as an image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return f'<img src="data:image/png;base64,{plot_url}"/>'

# --- HISTOGRAM (Rendered Chart) ---
@app.route('/histogram')
def histogram():
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

    return f'<img src="data:image/png;base64,{plot_url}"/>'

# === APP ENTRY POINT ===
if __name__ == '__main__':
    app.run(debug=True)