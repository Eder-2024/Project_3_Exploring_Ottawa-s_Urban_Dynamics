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

| Stakeholder                          | Key Questions Answered                                                                                       | Visualizations Used                                                                 | Recommendations                                                                                                                                    |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **🚔 Police & Traffic Enforcement**  | - Where are the high-collision hotspots? <br> - What day of the week are collisions most frequent? <br> - Impact of environmental conditions?  | - Interactive map <br> - Day-of-week bar charts <br> - Daily accidents by environmental condition charts | - Increase patrols and traffic control at hotspots. <br> - Schedule DUI checks and speed traps during risky weather and on Fridays. |
| **🏙️ Urban Planners & Local Councils** | - Which intersections and areas need redesign? <br> - Where do weather and infrastructure issues intersect?  | - Interactive map <br> - Heat maps <br> - Daily accidents by environmental condition charts | - Improve drainage and road treatments in snowy zones. <br> - Install smart traffic signals responsive to weather conditions. |
| **🚑 Emergency Services**            | - Where should emergency readiness be prioritized? <br> - What conditions lead to severe accidents?  | - Weather vs. accident severity charts <br> - Heatmap of accidents by location and traffic control | - Allocate emergency resources near high-severity zones such as intersections and areas with no traffic control (e.g., highways). <br> - Improve response readiness during hazardous weather, such as snow. |
| **📢 Educational Campaigners**       | - When do drivers need awareness the most? <br> - How does weather affect safe driving behavior?  | - Number of accidents by day of the week <br> - Number of accidents by hour of the day <br> - Daily accidents by environmental conditions | - Launch awareness campaigns during peak months (November to March) and rush hours (3-6 pm, school pickup and work close times). <br> - Tailor messages to weather-related risks (e.g., promote messages like: "Just because it’s not fatal doesn’t mean it’s safe"). |
| **🧠 Data for Research & Innovation** | - What patterns emerge? <br> - How can data support predictive modeling and policy change?  | - All visualizations, especially time-series and severity correlations | - Use findings to build AI-driven safety alerts. <br> - Support data-driven policies and innovations in transport safety. |
| **📦 Businesses & Logistics**        | - Which routes and times are safest for delivery operations?  | - Interactive maps | - Optimize delivery schedules around safe routes and times. <br> - Implement driver safety protocols during high-risk periods. <br> - Dynamically reroute trucks during snow events using weather-integrated GPS. |                      |

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

### Snow & Precipitation Impact (T-Tests)

Snow and precipitation significantly affect the number of vehicles involved in accidents:

### Weather & Fatalities (Linear Regression & Correlation)

All weather variables (tavg, wspd, prcp, snow) show statistically significant effects on the number of fatalities. 
However, the model has issues:
Negative R-squared (-inf): Likely due to constant values (fatalities always = 1), or small sample variation.
Multicollinearity warning: Weather variables may be too correlated with each other.
Still, significance (p < 0.05) implies a predictable, though weak, relationship.

### ☃️ Fatalities by Weather Category

Mean fatalities are exactly the same (1.0) for both Cold and Warm weather. This implies that the fatal accident severity may not be strongly based on weather.
This outcome could be due to the limitation of our dataset. Refer to limitation of dataset.

---
## Summary of Visualisation Charts

### 🔍 Interactive Map

The **interactive map** (rendered in HTML) displays the number of accidents that occurred at each location across Ottawa. Marker colors indicate the accident volume:

- 🟢 **Green** circle: Low number of accidents  
- 🟡 **Yellowish** circle: Medium number of accidents  
- 🟠 **Orange** circle: High number of accidents

Each map marker also includes a pop-up with detailed information on the severity of the incident:

- **Minimal**: Only superficial damage (e.g., scratches), with no medical intervention required.  
  *Marker: Green circle with an “i” inside.*

- **Minor**: Victims were assessed by ambulance staff but not taken to the hospital.  
  *Marker: Orange circle with an exclamation mark (!).*

- **Major**: Victims were transported to the hospital in critical or serious condition.  
  *Marker: Light red triangle with an exclamation mark (!).*

- ❌ **Fatal**: One or more individuals died either at the scene or later in the hospital.  
  *Marker: Dark red circle with an “x” inside.*

---

### 🔥 Heat Map

The **heat map** displays collision density throughout Ottawa. It uses gradient hues to represent the concentration of incidents:

- 🟢 **Green**: Low accident density  
- 🟠 **Amber**: Moderate accident density  
- 🔴 **Red**: High accident density

This map is accessible through a separate tab linked from the main visualizations HTML file.

---

- Scatter plot - Severity vs. Weather - This shoes the impact of the weather on the severity of accidents in terms of fatal, major, minor and minimal.

![Scatter Plot - Severity vs Weather](https://github.com/Eder-2024/Project_3_Exploring_Ottawa-s_Urban_Dynamics/blob/5c1492521eda73e9828ac5337b4947991569be02/Images/Scatter%20Plot%20-%20Severity%20vs%20Weather.png)

- Daily Accidents by Environmental conditions - This shows that in the winter months - snow led to high number of accidents on certain dates between Nvember and MaRCH with great fatalities.

![Daily Accidents by Environmental Conditions in 2020](https://github.com/Eder-2024/Project_3_Exploring_Ottawa-s_Urban_Dynamics/blob/5c1492521eda73e9828ac5337b4947991569be02/Images/Daily%20Accidents%20by%20Environmental%20Conditions%20in%202020.png)

- Top Dates chart - This shows the dates with the highest number of accidents are seen between November and March.

![top-dates-chart](https://github.com/Eder-2024/Project_3_Exploring_Ottawa-s_Urban_Dynamics/blob/5c1492521eda73e9828ac5337b4947991569be02/Images/top-dates-chart.png)

- Number of Accidents by Day of the week - This shows that most accidents happened on Friday and this couls be as a result that its the last day f the week with many celebrating TGIF, parties and some may be driving under influence.

![Number of Accidents by Day of the Week in 2020](https://github.com/Eder-2024/Project_3_Exploring_Ottawa-s_Urban_Dynamics/blob/5c1492521eda73e9828ac5337b4947991569be02/Images/Number%20of%20Accidents%20by%20Day%20of%20the%20Week%20in%202020.png)

- Number of Accidents by Hour of the Day - This shows the number o accidents happening during pick up schooltime and after closing works hours - 3pm - 6pm. 

![Number of Accidents by Hour of the Day](https://github.com/Eder-2024/Project_3_Exploring_Ottawa-s_Urban_Dynamics/blob/5c1492521eda73e9828ac5337b4947991569be02/Images/Number%20of%20Accidents%20by%20Hour%20of%20the%20Day.png)

- Heatmap of Accidents by Location and Control - This shows that about 50% of accidents happened at no intersectiona nd where ther eis no traffic control e.g. Highways. Then accidenta happened at inteserctiuon and intersection related even with traffic control. 

![Heatmap of Accidents by Location and Traffic Control](https://github.com/Eder-2024/Project_3_Exploring_Ottawa-s_Urban_Dynamics/blob/5c1492521eda73e9828ac5337b4947991569be02/Images/Heatmap%20of%20Accidents%20by%20Location%20and%20Traffic%20Control.png)

--

## Limitations of the Dataset

- The dataset covers only a single year, limiting the ability to identify long-term trends or seasonal patterns. A multi-year dataset would provide deeper insights and support more accurate predictive modeling.
- There is no information about drivers or vehicles involved in the collisions. This limits the ability to analyze contributing factors such as driver behavior, vehicle type, or condition.
- Weather data was matched by date only, not by the specific time of each accident. Since weather conditions can change rapidly within a day, this reduces the accuracy of correlation analysis between weather and collisions.

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

### 🚦 **Traffic Accident Data**  
**Source**: [City of Ottawa Open Data Portal](https://open.ottawa.ca/datasets/bf701649829642d28fa2e400a7136bdd_0/explore?location=45.249450%2C-75.797667%2C0.84)  
**License**: [Open Government License – City of Ottawa](https://open.ottawa.ca/pages/licence/)  
> The City of Ottawa provides free access to many of its datasets through a dedicated data portal.  
> The data is licensed under the **Open Government License**, making it easy to use and reuse.  
> For more information, visit [Open Ottawa](https://open.ottawa.ca)

### 🌤 **Weather Data**  
**Source**: [Meteostat – Ottawa Historical Weather](https://meteostat.net/en/place/ca/ottawa?s=71063&t=2020-01-01/2020-12-31)  
**License**:  
> Copyright © Meteostat  
> Weather data provided by **NOAA**, **Deutscher Wetterdienst**, and **Environment Canada**.  
> For full details, see [Meteostat Legal & Privacy](https://meteostat.net/en/about/legal).

This project itself is released under the **MIT License** for educational and research purposes.

---

> _"We can’t prevent every accident, but we can use data to give people the best chance to avoid them."_ – The Code Enforcers 🚗💨
