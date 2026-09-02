import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Flight Fare Prediction",
    page_icon="✈️",
    layout="centered"
)

# Load trained model
model = joblib.load("models/flight_fare_model.pkl")

# Title
st.title("✈️ Flight Fare Prediction")
st.write("Enter the flight details below to predict the fare.")

st.divider()

# Input fields
airline = st.selectbox(
    "Airline",
    ["SpiceJet", "AirAsia", "Vistara", "GO FIRST",
     "Indigo", "Air India", "Trujet", "StarAir"]
)

from_city = st.selectbox(
    "From",
    ["Delhi", "Mumbai", "Bangalore",
     "Kolkata", "Hyderabad", "Chennai"]
)

to_city = st.selectbox(
    "To",
    ["Mumbai", "Bangalore", "Kolkata",
     "Hyderabad", "Chennai", "Delhi"]
)

flight_class = st.selectbox(
    "Class",
    [0, 1]
)

day = st.number_input(
    "Day",
    min_value=1,
    max_value=31,
    value=15
)

month = st.selectbox(
    "Month",
    [2, 3]
)

dep_hour = st.number_input(
    "Departure Hour",
    min_value=0,
    max_value=23,
    value=10
)

arr_hour = st.number_input(
    "Arrival Hour",
    min_value=0,
    max_value=23,
    value=12
)

duration = st.number_input(
    "Flight Duration (minutes)",
    min_value=30,
    max_value=1500,
    value=120
)

stops = st.selectbox(
    "Number of Stops",
    [0, 1, 2]
)

st.divider()

# Prediction button
if st.button("🔮 Predict Flight Fare", use_container_width=True):

    # Create input dataframe
    input_data = pd.DataFrame({
        "airline": [airline],
        "from": [from_city],
        "to": [to_city],
        "class": [flight_class],
        "day": [day],
        "month": [month],
        "dep_hour": [dep_hour],
        "arr_hour": [arr_hour],
        "duration_in_min": [duration],
        "stops": [stops]
    })

    # Prediction
    prediction = model.predict(input_data)[0]

    # Display result
    st.success(
        f"💰 Predicted Flight Fare: ₹{prediction:,.2f}"
    )