import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🌾 Smart Farming Advisory System ")
crop = {
    'wheat': {
        'fertilizer': 'Urea with nitrogen source and DAP',
        'pesticides': 'Imidacloprid controls aphids and chlorpyrifos for soil insects',
        'climate': 'Low to moderate rainfall'
    },
    'rice': {
        'fertilizer': 'Urea for promoting leaf growth',
        'pesticides': 'Buprofezin',
        'climate': 'High rainfall'
    },
    'cotton': {
        'fertilizer': 'Nitrogen and Phosphorus',
        'pesticides': 'Thiamethoxam controls white fly',
        'climate': 'Moderate rainfall, warm and sunny'
    },
    'maize': {
        'fertilizer': 'DAP for 20–25 days',
        'pesticides': 'Spinosad controls leaf pests',
        'climate': 'Moderate rainfall and warm climate'
    },
    'sugarcane': {
        'fertilizer': 'MOP (Muriate of Potash)',
        'pesticides': 'Fipronil controls soil pests',
        'climate': 'Hot and humid with moderate rainfall'
    },
    'groundnut': {
        'fertilizer': 'DAP and Gypsum',
        'pesticides': 'Chlorpyrifos controls caterpillars',
        'climate': 'Low to moderate rainfall, warm and dry'
    },
    'paddy': {
        'fertilizer': 'Urea and DAP',
        'pesticides': 'Buprofezin controls plant hopper',
        'climate': 'Humid climate with standing water'
    },
    'sunflower': {
        'fertilizer': 'Nitrogen rich and single super phosphate',
        'pesticides': 'Quinalphos',
        'climate': 'Low rainfall, sunny and dry'
    }
}

yield_data = {
    'wheat': {'Black soil': 28, 'Red soil': 22, 'Alluvial soil': 35, 'Clay soil': 25},
    'rice': {'Black soil': 30, 'Red soil': 26, 'Alluvial soil': 38, 'Clay soil': 34},
    'cotton': {'Black soil': 32, 'Red soil': 24, 'Alluvial soil': 28, 'Clay soil': 20},
    'maize': {'Black soil': 26, 'Red soil': 23, 'Alluvial soil': 33, 'Clay soil': 27},
    'sugarcane': {'Black soil': 35, 'Red soil': 28, 'Alluvial soil': 30, 'Clay soil': 25},
    'groundnut': {'Black soil': 25, 'Red soil': 20, 'Alluvial soil': 30, 'Clay soil': 22},
    'paddy': {'Black soil': 32, 'Red soil': 28, 'Alluvial soil': 40, 'Clay soil': 35},
    'sunflower': {'Black soil': 20, 'Red soil': 18, 'Alluvial soil': 25, 'Clay soil': 22}
}


st.header("🌱 Select Crop")
crop_name = st.selectbox(
    "Choose a crop to get advice and compare yields:",
    list(crop.keys())
)

if st.button("Get Farming Advice"):
   
    st.subheader(f"🌾 Farming Recommendations for {crop_name.capitalize()}")
    st.write("**Fertilizer:**", crop[crop_name]["fertilizer"])
    st.write("**Pesticides:**", crop[crop_name]["pesticides"])
    st.write("**Climate:**", crop[crop_name]["climate"])

    st.subheader(f"🌡 Yield Heatmap for {crop_name.capitalize()} Across Soil Types")
    df = pd.DataFrame(yield_data[crop_name], index=[0]).T
    df.columns = ['Yield']
    fig, ax = plt.subplots()
    sns.heatmap(df, annot=True, cmap="YlGn", cbar=True)
    st.pyplot(fig)

    best_soil = max(yield_data[crop_name], key=yield_data[crop_name].get)
    st.success(f"✅ Best soil for {crop_name.capitalize()} is: {best_soil}")

    st.subheader("🌦 Weather Forecast (Next 7 Days)")
    st.write("Day 1–2: Sunny")
    st.write("Day 3–4: Partly Cloudy")
    st.write("Day 5: Light Rain")
    st.write("Day 6–7: Sunny")

    st.subheader("📌 General Farming Advice")
    st.write("• Water crops in early morning")
    st.write("• Avoid spraying pesticides during rain")
    st.write("• Use organic manure once a month")
