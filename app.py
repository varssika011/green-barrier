import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

st.title("AI for Corrosion Prevention")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

    # Train model
    X = data.drop("corrosion_rate", axis=1)
    y = data["corrosion_rate"]
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    st.success("Model trained successfully with uploaded file!")

    # Sliders for input
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
