import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load("Farm_Irrigation_System.pkl")

# Page config
st.set_page_config(page_title="Smart Irrigation System", layout="wide")

sensor_names = [
    "Soil Moisture - Zone A",
    "Soil Moisture - Zone B",
    "Soil Moisture - Zone C",
    "Soil Moisture - Zone D",
    "Soil Moisture - Zone E",
    "Temperature - Zone A",
    "Temperature - Zone B",
    "Humidity - Zone A",
    "Humidity - Zone B",
    "Rainfall Sensor - Zone A",
    "Rainfall Sensor - Zone B",
    "Light Intensity - Zone A",
    "Light Intensity - Zone B",
    "pH Level - Zone A",
    "pH Level - Zone B",
    "EC (Electrical Conductivity) - Zone A",
    "EC (Electrical Conductivity) - Zone B",
    "Wind Speed - Zone A",
    "Wind Speed - Zone B",
    "Leaf Wetness - Zone A"
]





# Sidebar
st.sidebar.title("About")
st.sidebar.info(
    """
     **Smart Irrigation System using ML**

    Adjust the sensor values and click predict to see which sprinklers will be turned ON/OFF.

    This project uses a trained ML model to decide irrigation needs for different crop zones.
    """
)

# Main title
st.title("Smart Sprinkler Prediction Panel")

# Layout: 2 columns
col1, col2 = st.columns([1, 1])

# Initialize sensor values
sensor_values = []

col1.subheader("🔧 Sensor Inputs (Scaled 0 to 1)")

with col1:
    for i in range(20):
        val = st.slider(sensor_names[i], 0.0, 1.0, 0.5, 0.01)
        sensor_values.append(val)

    if st.button("Set All to 0.5"):
        sensor_values = [0.5] * 20
        st.experimental_rerun()

# Prediction
if st.button(" Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    with col2:
        st.subheader("Prediction Results")
        for i, status in enumerate(prediction):
            color = "green" if status == 1 else "red"
            state = "ON" if status == 1 else "OFF "
            st.markdown(
                f"<span style='color:{color}; font-weight:600;'>Sprinkler {i} (parcel_{i}): {state}</span>",
                unsafe_allow_html=True
            )
else:
    with col2:
        st.info("Press 'Predict Sprinklers' to see the results.")


