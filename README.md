# 🚦 Ottawa Traffic Collision & Weather Insight Analysis (2020)
## Group 5 – *The Code Enforcers* 🚗💨

<p align="center">
  <img src="https://img.shields.io/badge/Flask-%23000.svg?style=for-the-badge&logo=Flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite3-%234B6E60.svg?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" />
  <img src="https://img.shields.io/badge/Seaborn-%231572B6.svg?style=for-the-badge&logo=Seaborn&logoColor=white" />
  <img src="https://img.shields.io/badge/Folium-%234CAF50.svg?style=for-the-badge&logo=folium&logoColor=white" />
  <img src="https://img.shields.io/badge/Scipy-%230C2340.svg?style=for-the-badge&logo=scipy&logoColor=white" />
  <img src="https://img.shields.io/badge/Statsmodels-%23008080.svg?style=for-the-badge&logo=statsmodels&logoColor=white" />
  <img src="https://img.shields.io/badge/Base64-%23ff5c8e.svg?style=for-the-badge&logo=base64&logoColor=white" />
  <img src="https://img.shields.io/badge/HeatMap-%234CAF50.svg?style=for-the-badge&logo=folium&logoColor=white" />
  <img src="https://img.shields.io/badge/MarkerCluster-%234CAF50.svg?style=for-the-badge&logo=folium&logoColor=white" />
</p>
---

### 💡 Introduction

One of the things we all dread is being in a meeting and getting a call that a loved one was involved in a car accident—be it fatal or not. 

Bearing that in mind, **Group 5 – The Code Enforcers** decided to analyze Ottawa's 2020 traffic collision data alongside weather data to uncover patterns, causes, and high-risk conditions. Our goal: to foretell and prevent accidents through data-driven storytelling and visual insight, ensuring everyone gets to their destination safely.

_"We can’t prevent every accident, but we can use data to give people the best chance to avoid them."_ – The Code Enforcers 🚗💨

---

### 📊 Project Overview

Using publicly available datasets from the City of Ottawa and Meteostat, we created an interactive, data-rich visual narrative exploring **when, where, and why** accidents occurred.

The merged dataset gave us the power to explore the relationship between **weather conditions**, **time of day**, **collision location**, and **accident severity**. 

Through insightful visualizations built with **Python, Pandas, Seaborn, Folium, Scipy, Statsmodels, Base64 and Matplotlib**, powered by **SQLite** and a **Flask API**, we turn raw data into meaningful stories and actionable insights.

---

### 🎯 Stakeholder Focus & Questions Answered

| Stakeholder               | Questions Answered | Visualizations Used              | Recommendations
|--------------------------|--------------------|---------------------|
| **🚔 Police & Traffic Enforcement** | Where are the high-collision hotspots? <br> What day of the week are collisions most frequent? Impact of environmental conditions?| - Interactive map and correlation <br> - Day-of-the-week bar charts  <br> - Daily Accident by environmental condition charts| Increase patrols at high-collision spots and traffic conrol where there are none. <br> Consider more frequent DUI checks or speed traps during risky weather conditions and especially Fridays.
| **🏙️ Urban Planners & Local Councils** | Which intersections and areas need redesign? Is there a difference between urban and rural collisions? | - Geographic scatter plots <br> - Collision density heatmaps |
| **🚑 Emergency Services** | Where should we prioritize emergency readiness? What conditions lead to severe accidents? | - Weather vs. severity folium marker <br> - Trend lines by road surface & lighting |
| **📢 Educational Campaigners** | When do drivers need awareness the most? How does weather affect safe driving? | - Line plots with Viridis colors <br> - Monthly trends and rush-hour charts |
| **🧠 Data for Research & Innovation**
| **📦 Businesses & Logistics** | Which routes and times are safest for delivery operations? | - Interactive Accident map|

---

### 🗃️ Data Sources

- [Ottawa Motor Vehicle Collisions 2020 (Open Ottawa)](https://open.ottawa.ca/datasets/bf701649829642d28fa2e400a7136bdd_0/explore)
- [Ottawa Daily Weather 2020 (Meteostat)](https://meteostat.net/en/place/ca/ottawa?s=71063&t=2020-01-01/2020-12-31)

Merged on date to correlate weather with accidents.

---

### 🧰 Technologies & Tools

- **Python** (Pandas, Seaborn, Matplotlib, Folium)
- **Flask** backend serving dynamic visualizations
- **SQLite3** for relational database storage
- **Jupyter Notebook** for EDA and story creation
- **HTML + CSS** for simple frontend interaction

---

## 🛠️ Installation & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/Eder-2024/Project_3_Exploring_Ottawa-s_Urban_Dynamics.git
cd Project_3_Exploring_Ottawa-s_Urban_Dynamics
```
---

### 2. Install Required Python Libraries

Make sure you have **Python 3.8+** and **pip** installed. Then run:

```bash
pip install flask pandas matplotlib seaborn folium statsmodels scipy
```
---
## 🧠 Project Structure
```
Project_3_Exploring_Ottawa-s_Urban_Dynamics/
│
├── app.py                 # Flask app - main backend logic
├── mainCode.ipynb         # Jupyter notebook for EDA and testing
├── accidents.db           # SQLite database with accident + weather data
│
├── templates/
│   └── index.html         # HTML template for the dashboard
│
├── static/
│   └── style.css          # Custom CSS styles
```
---
## 🚀 How to Run the App
You can run this app either via **Visual Studio Code** or the **Windows Command Prompt**:
---
### ✅ Option 1: Using Visual Studio Code (VS Code)
1. Open **VS Code**.
2. Open the project folder:  
   `Project_3_Exploring_Ottawa-s_Urban_Dynamics/`
3. Open `app.py`.
4. Run the app:
   - Open the terminal and run:
     ```bash
     python app.py
     ```
5. Go to your browser and visit:  
   👉 `http://127.0.0.1:5000`
---
### 🖥️ Option 2: Using Windows Command Prompt (CMD)
1. Open **Command Prompt**.
2. Navigate to the project folder:
   ```bash
   cd path\to\Project_3_Exploring_Ottawa-s_Urban_Dynamics
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open your browser and go to:  
   👉 `http://127.0.0.1:5000`
   
## 📉 Summary Findings 📈

## Summary of Statistical Analysis 

### Objectives: xxx

## Snow & Precipitation Impact (T-Tests)

Snow and precipitation significantly affect the number of vehicles involved in accidents:

- Extremely low p-values (< 0.00001) indicate strong statistical evidence that both snow and rain contribute to higher accident volumes.
  - **Snow →** More accidents (positive t-statistic)
  - **Precipitation →** Fewer accidents (negative t-statistic — likely due to more cautious driving in rain)

---

## Weather & Fatalities (Linear Regression)

All weather variables (tavg, wspd, prcp, snow) show statistically significant effects on the number of fatalities. 

However, the model has issues:
- **Negative R-squared (-inf):** Likely due to constant values (fatalities always = 1), or small sample variation.
- **Multicollinearity warning:** Weather variables may be too correlated with each other.

Still, significance (p < 0.05) implies a predictable, though weak, relationship.

---

## ☃️ Fatalities by Weather Category

Mean fatalities are exactly the same (1.0) for both Cold and Warm weather:

- Suggests that fatal accident severity is not strongly weather-dependent in your current dataset — could be due to limited variance or sample size.


## Summary of Visualisation Charts 
- xxx
--

## Recommendations:
- xxx

### 🚔 1. Police & Traffic Enforcement
- **Insight:** Snow conditions significantly increase accident volume.
- **Action:**
  - Increase patrols during snowfall and icy conditions.
  - Set up temporary enforcement zones or automated alerts during winter storms.
  - Consider more frequent DUI checks or speed traps during risky weather conditions.

### 🌆 2. Urban Planners & Local Councils
- **Insight:** Snowy conditions result in more accidents, but fatalities don’t vary much between warm/cold.
- **Action:**
  - Improve road treatment and drainage in high-snowfall zones.
  - Add smart traffic signals that adapt to weather inputs.
  - Prioritize infrastructure upgrades in areas with high vehicle counts during snow.

### 🚑 3. Emergency Services
- **Insight:** Snow and precipitation correlate with more multi-vehicle accidents.
- **Action:**
  - Route EMS services to avoid congested accident-prone roads during snowstorms.
  - Use predictive weather data to staff accordingly for expected spikes in accidents.

### 📢 4. Educational Campaigns
- **Insight:** Accident counts rise during snow, even if fatalities don’t.
- **Action:**
  - Focus campaigns on defensive driving in winter.
  - Promote messages like: "Just because it’s not fatal doesn’t mean it’s safe."
  - Run these campaigns ahead of snowy seasons.

### 🧠 5. Data for Research & Innovation
- **Insight:** Strong statistical relationship between snow and accident counts, but weak link with fatality variation.
- **Action:**
  - Use this as a foundation for machine learning models predicting accident risk.
  - Feed into smart city simulations and test how autonomous vehicles behave in snow/precipitation scenarios.

### 🏢 6. Businesses & Logistics
- **Insight:** Snow is a high-risk condition for delivery fleets.
- **Action:**
  - Dynamically reroute trucks during snow events using weather-integrated GPS.
  - Adjust delivery windows and avoid sending vehicles during peak snow hours.

---

### 🧭 Ethical Considerations

- We anonymized any personally identifiable information.
- Data is used strictly for **public safety research**, **education**, and **urban improvement**.
- We advocate **responsible communication** of insights to avoid misuse or misinterpretation, especially when suggesting enforcement or planning actions.

---

### 🔗 References

- Open Ottawa: Motor Vehicle Collision Data
- Meteostat: Historical Weather Data
- Stack Overflow & Matplotlib docs for coding patterns
- [Color Universal Design](https://jfly.uni-koeln.de/color/) for accessible visual palettes

---

### 🙌 Contributors – Group 5: The Code Enforcers

- Eder Ortiz  (In charge of coding, data cleaning, and generating visualizations)
- Geraldine Valencia (In charge of coding and interactive map visualization)
- Demilade Adenuga  (In charge of developing visualizations and writing summaries)

---
## 📚 License & Data Sources

This project uses open data provided by two official sources:

---

### 🚦 **Traffic Accident Data**  
**Source**: [City of Ottawa Open Data Portal](https://open.ottawa.ca/datasets/bf701649829642d28fa2e400a7136bdd_0/explore?location=45.249450%2C-75.797667%2C0.84)  
**License**: [Open Government License – City of Ottawa](https://open.ottawa.ca/pages/licence/)  

> The City of Ottawa provides free access to many of its datasets through a dedicated data portal.  
> The data is licensed under the **Open Government License**, making it easy to use and reuse.  
> For more information, visit [Open Ottawa](https://open.ottawa.ca).

---

### 🌤 **Weather Data**  
**Source**: [Meteostat – Ottawa Historical Weather](https://meteostat.net/en/place/ca/ottawa?s=71063&t=2020-01-01/2020-12-31)  
**License**:  
> Copyright © Meteostat  
> Weather data provided by **NOAA**, **Deutscher Wetterdienst**, and **Environment Canada**.  
> For full details, see [Meteostat Legal & Privacy](https://meteostat.net/en/about/legal).

---

This project itself is released under the **MIT License** for educational and research purposes.

---

> _"We can’t prevent every accident, but we can use data to give people the best chance to avoid them."_ – The Code Enforcers 🚗💨
