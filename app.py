import plotly.graph_objects as go


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from datetime import date


def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


# Page Configuration

st.set_page_config(
    page_title="AQI Smart City Dashboard",
    page_icon="🌍",
    layout="wide"
)


# Load Model


@st.cache_resource
def load_model():
    return joblib.load("aqi_model.pkl")

model = load_model()


# Load Dataset


@st.cache_data
def load_data():
    df = pd.read_csv("india_city_aqi_2015_2023.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()



# City Coordinates


city_coordinates = {
    "Ahmedabad": [23.0225, 72.5714],
    "Bengaluru": [12.9716, 77.5946],
    "Chennai": [13.0827, 80.2707],
    "Delhi": [28.6139, 77.2090],
    "Hyderabad": [17.3850, 78.4867],
    "Jaipur": [26.9124, 75.7873],
    "Kolkata": [22.5726, 88.3639],
    "Lucknow": [26.8467, 80.9462],
    "Mumbai": [19.0760, 72.8777],
    "Pune": [18.5204, 73.8567]
}


# Sidebar



st.sidebar.image("logo.png", use_container_width=True)
st.sidebar.title("🌍 AQI Dashboard")


st.sidebar.markdown("### Project Information")

st.sidebar.write("**Model:** Random Forest Regressor")
st.sidebar.write("**Dataset:** India AQI 2015-2023")
st.sidebar.write("**Developer:**")
st.sidebar.write("Shubham Kumar")
st.sidebar.write("Ayushi Raj")

st.sidebar.write("**Today's Date:**", date.today())
st.sidebar.write("**Total Records:**", len(df))
st.sidebar.write("**Total Cities:**", df["city"].nunique())



# Title

st.markdown("""
<div style="
background:linear-gradient(90deg,#1E3C72,#2A5298);
padding:20px;
border-radius:15px;
text-align:center;
color:white;">
<h1>🌍 AQI Smart City Dashboard</h1>
<p>Predict Air Quality Index using Machine Learning</p>
</div>
""", unsafe_allow_html=True)



col1, col2, col3, col4 = st.columns(4)

col1.metric("🏙 Cities", df["city"].nunique())
col2.metric("📄 Records", len(df))
col3.metric("📅 Years", "2015-2023")
col4.metric("🤖 Model", "Random Forest")

st.subheader("📊 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "🌍 Cities",
    df["city"].nunique()
)

col2.metric(
    "📄 Total Records",
    len(df)
)

col3.metric(
    "📈 Average AQI",
    round(df["aqi"].mean(), 2)
)

col4.metric(
    "🏭 Highest AQI",
    int(df["aqi"].max())
)




# Select City



cities = sorted(df["city"].unique())

selected_city = st.selectbox(
    "🏙️ Select City",
    cities
)


# Date Filter



min_date = df["date"].min().date()
max_date = df["date"].max().date()

start_date, end_date = st.date_input(
    "📅 Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)


# Input Form



with st.form("aqi_form"):

    pm25 = st.number_input("PM2.5", 0.0, 500.0, 50.0)
    pm10 = st.number_input("PM10", 0.0, 500.0, 100.0)
    no2 = st.number_input("NO₂", 0.0, 200.0, 30.0)
    so2 = st.number_input("SO₂", 0.0, 100.0, 10.0)
    co = st.number_input("CO", 0.0, 10.0, 0.5)
    o3 = st.number_input("O₃", 0.0, 200.0, 40.0)

    predict = st.form_submit_button("Predict AQI")


# Prediction



if predict:

    
    with st.spinner("🔄 Predicting AQI... Please wait."):
     prediction = model.predict([[pm25, pm10, no2, so2, co, o3]])
    aqi = prediction[0]
    st.success("✅ AQI Prediction Completed Successfully!")

    st.header("Prediction Result")

    st.metric("Predicted AQI", f"{aqi:.2f}")

    

    # AQI Gauge

    st.subheader("🌡️ AQI Gauge")

    fig = go.Figure(go.Indicator(
      mode="gauge+number",
      value=aqi,
      title={"text": "Predicted AQI"},
      gauge={
        "axis": {"range": [0, 300]},
        "bar": {"color": "darkblue"},
        "steps": [
            {"range": [0, 50], "color": "green"},
            {"range": [50, 100], "color": "yellow"},
            {"range": [100, 150], "color": "orange"},
            {"range": [150, 200], "color": "red"},
            {"range": [200, 300], "color": "purple"}
        ]}
     ))


    st.plotly_chart(fig, use_container_width=True)

    st.write("**Selected City:**", selected_city)

    progress = min(int(aqi / 300 * 100), 100)

    st.progress(progress)





    # AQI Status



    if aqi <= 50:
        st.success("🟢 Good")
        st.write("Air quality is good.")

    elif aqi <= 100:
        st.info("🟡 Satisfactory")
        st.write("Air quality is acceptable.")

    elif aqi <= 150:
        st.warning("🟠 Moderate")
        st.write("Sensitive people should reduce outdoor activity.")

    elif aqi <= 200:
        st.warning("🔴 Poor")
        st.write("Wear a mask outdoors.")

    else:
        st.error("🚨 Very Poor / Severe")
        st.write("Avoid outdoor activities.")




    
    
    # Filter City and Date
    


    city_data = df[df["city"] == selected_city].copy()

    city_data = city_data[
    (city_data["date"] >= pd.to_datetime(start_date)) &
    (city_data["date"] <= pd.to_datetime(end_date))
        ]
    
    
    city_data = city_data.sort_values("date")

    
    
    if city_data.empty:
      st.warning("No data available for the selected date range.")
      st.stop()


    # AQI Trend

    
    
    st.markdown(
    "<h2 style='color:#1E88E5;'>📈 AQI Trend</h2>",
    unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(12,5))

    ax.plot(
        city_data["date"],
        city_data["aqi"],
        linewidth=2
    )

    ax.set_title(f"{selected_city} AQI Trend")

    ax.set_xlabel("Date")

    ax.set_ylabel("AQI")

    plt.xticks(rotation=45)

    st.pyplot(fig)

    plt.close(fig)

   


    # Statistics


    
    with st.container():

     st.subheader("📊 City Statistics")

    c1,c2,c3=st.columns(3)

    c1.metric("Average AQI",round(city_data["aqi"].mean(),2))
    c2.metric("Maximum AQI",city_data["aqi"].max())
    c3.metric("Minimum AQI",city_data["aqi"].min())
    

    st.subheader("📌 AQI Insights")

    highest_aqi = city_data.loc[city_data["aqi"].idxmax()]
    lowest_aqi = city_data.loc[city_data["aqi"].idxmin()]

    col1, col2 = st.columns(2)

    with col1:
     st.success(f"🌿 Best Air Quality\n\nDate: {lowest_aqi['date'].date  ()}\nAQI: {lowest_aqi['aqi']}")

    with col2:
     st.error(f"🏭 Worst Air Quality\n\nDate: {highest_aqi['date'].date()}\nAQI: {highest_aqi['aqi']}")
    




    # Interactive Map



    st.subheader("🗺️ City Location")

    if selected_city in city_coordinates:

     map_df = pd.DataFrame({
        "lat":[city_coordinates[selected_city][0]],
        "lon":[city_coordinates[selected_city][1]],
        "AQI":[round(aqi,2)]
       })
        

     st.map(map_df, zoom=10)

     st.success(f"{selected_city} - Predicted AQI: {aqi:.2f}")

    else:
        st.warning("Location not available.")
      

    # Pollutant Chart
    


    st.subheader("🧪 Average Pollutant Levels")

    pollutants = ["pm25","pm10","no2","so2","co","o3"]

    avg_pollutants = city_data[pollutants].mean()

    st.bar_chart(avg_pollutants)

    

    # AQI Category Distribution


    
    st.subheader("🥧 AQI Category Distribution")

    category_counts = city_data["aqi_category"].value_counts()

    st.bar_chart(category_counts)


    # Dataset
    

    st.subheader("📋 Data for Selected City")

    st.dataframe(
    city_data.sort_values("date", ascending=False).head(20))

    


    # Download Button
    
    csv = city_data.to_csv(index=False)

    st.download_button(
        label="📥 Download City Data",
        data=csv,
        file_name=f"{selected_city}_AQI.csv",
        mime="text/csv"
    )

    st.markdown("---")

    st.markdown("""
    <center>
    Made with ❤️ using Streamlit | AQI Smart City Dashboard<br>
    Developed by <b>Shubham Kumar & Ayushi Raj</b>
    </center>
    """, unsafe_allow_html=True)
