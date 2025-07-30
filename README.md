# Smart Irrigation System using Machine Learning

A zone-wise smart irrigation system that uses machine learning to predict which areas of a field need irrigation, helping reduce water wastage and increase crop yield. Built with Python and Streamlit, the system allows real-time user interaction using sensor data.

---


## Overview

The system collects environmental data from multiple zones in an agricultural field (like soil moisture, temperature, humidity, etc.) and feeds it into a trained ML model. The model predicts whether irrigation is needed in each zone and controls the respective sprinkler.

Users can manually input scaled sensor values through a Streamlit web interface and get real-time sprinkler status.

---

## Features

- Zone-wise sensor input (20 sensors for multiple environmental factors)
- ML-based decision on sprinkler ON/OFF
- Streamlit-powered user interface with sliders and live prediction
- Scaled input support for standardized predictions
- Clean UI with intuitive sensor labeling

---

## Tech Stack

| Component     | Tool / Library                  |
|---------------|---------------------------------|
| ML Algorithm  | Random Forest / Decision Tree   |
| Backend       | Python                          |
| UI            | Streamlit                       |
| Serialization | joblib (for model saving/loading) |
| Hardware (Optional) | Soil sensors, Raspberry Pi, etc. |

---

## Sensor Mapping

| Index | Sensor Name                         |
|-------|-------------------------------------|
| 0     | Soil Moisture - Zone A              |
| 1     | Soil Moisture - Zone B              |
| 2     | Soil Moisture - Zone C              |
| 3     | Soil Moisture - Zone D              |
| 4     | Soil Moisture - Zone E              |
| 5     | Temperature - Zone A                |
| 6     | Temperature - Zone B                |
| 7     | Humidity - Zone A                   |
| 8     | Humidity - Zone B                   |
| 9     | Rainfall Sensor - Zone A            |
| 10    | Rainfall Sensor - Zone B            |
| 11    | Light Intensity - Zone A            |
| 12    | Light Intensity - Zone B            |
| 13    | pH Level - Zone A                   |
| 14    | pH Level - Zone B                   |
| 15    | EC (Electrical Conductivity) - Zone A |
| 16    | EC (Electrical Conductivity) - Zone B |
| 17    | Wind Speed - Zone A                 |
| 18    | Wind Speed - Zone B                 |
| 19    | Leaf Wetness - Zone A               |

---

## Installation

### 

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-irrigation-ml.git
   cd smart-irrigation-ml
2. Install dependencies:


  ```bash
  pip install -r requirements.txt



```
  pip install streamlit
  pip install numpy
  pip install scikit-learn
  pip install joblib
  Make sure you are using Python 3.7 or higher.



Usage
Ensure the trained model file (Farm_Irrigation_System.pkl) is in the same folder as app.py.

Run the Streamlit app:

```streamlit run app.py
Open in your browser (http://localhost:8501)

Use the sliders to set values for each zone-wise sensor.

Click "Predict Sprinklers" to see which sprinklers turn ON/OFF based on ML prediction.