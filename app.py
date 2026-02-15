import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import numpy as np

# Train model (or load if already saved)
def train_model():
    # Adjust path if your CSV is not inside a "data" folder
    data = pd.read_csv("data/corrosion_data.csv")
    X = data.drop("corrosion_rate", axis=1)
    y = data["corrosion_rate"]
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    joblib.dump(model, "corrosion_model.pkl")
    return model

# Try loading the model, otherwise train a new one
try:
    model = joblib.load("corrosion_model.pkl")
except FileNotFoundError:
    model = train_model()

# Streamlit UI
st.title("AI for Corrosion Prevention")

humidity = st.slider("Humidity (%)", 0, 100, 50)
salinity = st.slider("Salinity (ppm)", 0, 5000, 1000)
temperature = st.slider("Temperature (°C)", -20, 100, 25)  # ✅ fixed syntax
pH = st.slider("pH", 0, 14, 7)

if st.button("Predict"):
    features = np.array([[humidity, salinity, temperature, pH]])
    prediction = model.predict(features)[0]
    st.write("Predicted corrosion rate:", prediction)
sss
