# 🌍 AQI Smart City Dashboard

A Machine Learning-powered web application developed using **Python** and **Streamlit** to predict the **Air Quality Index (AQI)** based on pollutant concentrations. The dashboard provides interactive visualizations, city-wise analysis, AQI trends, maps, and health recommendations to help users understand air quality conditions.

---

## 📖 Project Overview

Air pollution is a major environmental and public health concern. This project predicts the Air Quality Index (AQI) using machine learning and presents the results through an interactive dashboard. Users can select a city, enter pollutant values, visualize AQI trends, explore statistics, and download city-specific data.

---

## 🎯 Objectives

- Predict AQI using Machine Learning.
- Visualize AQI trends for different cities.
- Analyze pollutant levels.
- Provide health recommendations based on AQI.
- Support Smart City environmental monitoring.

---

## ✨ Features

- 🤖 AQI Prediction using Machine Learning
- 🌡️ AQI Gauge Visualization
- 🏙️ City Selection
- 📅 Date Range Filter
- 📈 AQI Trend Analysis
- 📊 Monthly AQI Trend
- 📍 Interactive City Map
- 📋 City Statistics
- 🧪 Pollutant Comparison Chart
- 🥧 AQI Category Distribution
- 📌 AQI Insights
- 📥 Download City Data (CSV)
- 💡 Health Recommendations
- 🎨 Modern Streamlit Dashboard
- ⏳ Loading Animation
- ✅ Success Notification

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Plotly
- Scikit-learn
- Joblib

---

## 📂 Dataset

**Dataset:** India AQI Dataset (2015–2023)

Dataset contains the following information:

- City
- Date
- PM2.5
- PM10
- NO₂
- SO₂
- CO
- O₃
- AQI
- AQI Category

---

## 🤖 Machine Learning Model

The AQI prediction model was trained using a supervised Machine Learning regression algorithm on historical AQI and pollutant data.

### Input Features

- PM2.5
- PM10
- NO₂
- SO₂
- CO
- O₃

### Output

- Predicted AQI



## 📊 Dashboard Modules

### 🌍 Dashboard Overview

Displays project information and dataset summary.

### 🤖 AQI Prediction

Predicts AQI from pollutant concentrations.

### 🌡️ AQI Gauge

Visual indicator of predicted AQI level.

### 📈 AQI Trend

Shows historical AQI trend for the selected city.

### 📊 Statistics

Displays:

- Average AQI
- Maximum AQI
- Minimum AQI

### 🧪 Pollutant Analysis

Visualizes average pollutant concentrations.

### 🗺️ Interactive Map

Displays the selected city's location.

### 📌 AQI Insights

Highlights the best and worst AQI days for the selected city.

### 📋 Data Table

Displays city-specific AQI records.

### 📥 Download

Allows users to download city data as a CSV file.


## 📁 Project Structure

AQI_Smart_City_AI/
│── app.py
│── aqi_model.pkl
│── india_city_aqi_2015_2023.csv
│── style.css
│── logo.png
│── requirements.txt
│── README.md


## ⚙️ Installation

### Clone the repository

```bash
git clone <repository-link>
```

### Move to the project folder

```bash
cd AQI_Smart_City_AI
```

### Install required packages

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```




## 📌 Important Note

Due to GitHub's file size limit, the trained machine learning model (`aqi_model.pkl`) is not included in this repository.

To regenerate the model:

1. Download the dataset.
2. Open the training notebook (`.ipynb`) in Google Colab or Jupyter Notebook.
3. Run all cells to train the Random Forest Regressor.
4. Save the trained model using:

```python
import joblib

joblib.dump(model, "aqi_model.pkl")
```

After generating the model, place `aqi_model.pkl` in the project folder before running the Streamlit application.





## 📈 Future Scope

- Live AQI data integration
- Weather API integration
- AQI forecasting
- Mobile-responsive dashboard
- Email alerts
- Multi-city comparison
- Real-time pollution monitoring

---

## 👨‍💻 Developers

**Shubham Kumar**

**Ayushi Raj**

---

## 📄 License

This project is developed for educational and hackathon purposes.

---

## 🙏 Acknowledgements

- Streamlit
- Scikit-learn
- Pandas
- Plotly
- Kaggle
- Open-source Python Community