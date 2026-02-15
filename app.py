import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import os

# Train model directly from dataset
def train_model():
    # Build a safe path to the CSV file
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "data", "corrosion_data.csv")

    # Read the dataset
    data = pd.read_csv(file_path)

    # Split into features and target
    X = data.drop("corrosion_rate", axis=1)
    y = data["corrosion_rate"]

    # Train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

# Train once at startup
model = train_model()

# Streamlit UI
st.title("AI for Corrosion Prevention")

humidity = st.slider("Humidity (%)", 0, 100, 50)
salinity = st.slider("Salinity (ppm)", 0, 5000, 1000)
temperature = st.slider("Temperature (°C)", -20, 100, 25)
pH = st.slider("pH", 0, 14, 7)

if st.button("Predict"):
    input_data = pd.DataFrame({
        "humidity": [humidity],
        "salinity": [salinity],
        "temperature": [temperature],
        "pH": [pH]
    })
    prediction = model.predict(input_data)[0]
    st.write("Predicted corrosion rate:", round(prediction, 2))
