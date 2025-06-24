import streamlit as st
import pickle
import numpy as np

# Load model
with open('weather_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🌧️ Rain Prediction App")

# Take inputs (must match model's training features exactly)
MinTemp = st.number_input("Min Temperature")
MaxTemp = st.number_input("Max Temperature")
Rainfall = st.number_input("Rainfall")
Humidity3pm = st.number_input("Humidity at 3 PM")
WindGustSpeed = st.number_input("Wind Gust Speed")
RainToday = st.selectbox("Did it rain today?", ["No", "Yes"])

# Encode 'RainToday' as 0/1 like training
RainToday_encoded = 1 if RainToday == "Yes" else 0

# Make prediction
if st.button("Predict"):
    # Feature order must match training
    input_data = np.array([[MinTemp, MaxTemp, Rainfall, Humidity3pm, WindGustSpeed, RainToday_encoded]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("☔ It will rain tomorrow.")
    else:
        st.info("☀️ No rain tomorrow.")
