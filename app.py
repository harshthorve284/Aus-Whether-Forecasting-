
import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('gradient_boost_model.pkl')

st.title("🌧️ Rain Prediction App")
st.write("Predict whether it will rain tomorrow based on weather conditions.")

# Inputs (sample features, replace with your actual ones)
Rainfall = st.number_input("Rainfall (mm)", 0.0, 100.0)
Humidity3pm = st.slider("Humidity at 3pm (%)", 0, 100)
RainToday = st.selectbox("Did it rain today?", ['Yes', 'No'])

# Convert input
RainToday_binary = 1 if RainToday == 'Yes' else 0

# Predict
if st.button("Predict"):
    input_data = np.array([[Rainfall, Humidity3pm, RainToday_binary]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("🌧️ It **will rain** tomorrow.")
    else:
        st.info("☀️ It **won't rain** tomorrow.")
