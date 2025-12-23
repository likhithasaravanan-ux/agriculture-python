import streamlit as st

st.title("🌾 Smart Farming Advisory System")

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

st.header("🌱 Select Soil Type")

soil = st.selectbox(
    "Choose your soil type:",
    ["Black soil", "Red soil", "Alluvial soil", "Clay soil"]
)

crop_options = {
    "Black soil": ["cotton", "sugarcane"],
    "Red soil": ["wheat", "rice"],
    "Alluvial soil": ["maize", "groundnut"],
    "Clay soil": ["sunflower", "paddy"]
}

selected_crop = st.selectbox(
    "Choose the crop:",
    crop_options[soil]
)

if st.button("Get Farming Advice"):
    st.subheader("🌾 Crop Recommendations")
    st.write("**Fertilizer:**", crop[selected_crop]["fertilizer"])
    st.write("**Pesticides:**", crop[selected_crop]["pesticides"])
    st.write("**Climate:**", crop[selected_crop]["climate"])

    st.subheader("🌦 Weather Forecast (Next 7 Days)")
    st.write("Day 1–2: Sunny")
    st.write("Day 3–4: Partly Cloudy")
    st.write("Day 5: Light Rain")
    st.write("Day 6–7: Sunny")

    st.subheader("📌 General Farming Advice")
    st.write("• Water crops in early morning")
    st.write("• Avoid spraying pesticides during rain")
    st.write("• Use organic manure once a month")

