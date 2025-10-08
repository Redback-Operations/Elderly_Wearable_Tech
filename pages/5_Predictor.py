# pages/3_Predictor.py

import streamlit as st
import joblib
import numpy as np
import speech_recognition
import translate
import plotly
import pywaffle
import joblib


st.set_page_config(page_title="Predictor", page_icon="🧠")

def show_predictor():
    st.header("📊 Obesity Risk Prediction (Caregiver Friendly)")

    st.markdown("""
    _Please enter the child’s lifestyle details. We’ll estimate the risk and suggest simple actions._  
    """)

    # Inputs
    screen_time = st.slider("📱 Daily screen time (hours)", 0, 12, 4)
    physical_activity = st.slider("🏃 Physical activity (mins/day)", 0, 180, 30)
    sleep_duration = st.slider("😴 Sleep duration (hours)", 0, 12, 8)
    diet_quality = st.selectbox("🍽️ Diet quality", ["Poor", "Average", "Good"])
    income = st.selectbox("💰 Household income", ["Low", "Medium", "High"])
    location = st.selectbox("📍 Location", ["Urban", "Regional", "Remote"])

    # Encode inputs
    diet_map = {"Poor": 1, "Average": 2, "Good": 3}
    income_map = {"Low": 0, "Medium": 1, "High": 2}
    location_map = {"Urban": 0, "Regional": 1, "Remote": 2}

    input_data = [
        screen_time,
        physical_activity,
        sleep_duration,
        diet_map[diet_quality],
        income_map[income],
        location_map[location]
    ]

    # Predict
    if st.button("🔍 Predict Risk"):
        try:
            model = joblib.load("models/classifier.pkl")
            features = joblib.load("models/feature_names.pkl")
            weights = joblib.load("models/feature_weights.pkl")

            prediction = model.predict([input_data])[0]
            probas = model.predict_proba([input_data])[0]

            class_map = {0: "Low", 1: "Medium", 2: "High"}
            st.success(f"**Predicted Risk: {class_map[prediction]}**")
            st.progress(int(probas[prediction] * 100))

            # Show top contributors
            st.markdown("### 🔍 Top 3 Risk Contributors")
            top3 = np.argsort(weights)[::-1][:3]
            explanations = {
                "screen_time": "High screen time is linked with inactivity and weight gain.",
                "physical_activity": "Exercise helps burn calories and maintain fitness.",
                "sleep_duration": "Poor sleep affects hormones that control appetite.",
                "diet_quality": "Low-nutrient foods can lead to unhealthy weight gain.",
                "income": "Income may affect access to healthy food or sports.",
                "location": "Environment can influence diet and exercise options."
            }
            for i in top3:
                name = features[i]
                st.markdown(f"- **{name.replace('_',' ').title()}**: {round(weights[i]*100, 2)}% — {explanations.get(name, '')}")

            # Friendly tips
            st.markdown("### 📢 Simple Caregiver Tips")
            if screen_time > 4 and physical_activity < 30:
                st.warning("⚠️ Try reducing screen time and encouraging outdoor play.")
            if diet_map[diet_quality] == 1:
                st.warning("🍭 Swap sugary snacks for fruits or home-cooked food.")
            if sleep_duration < 7:
                st.warning("🛌 Encourage a consistent 8–10 hr sleep routine.")
            if prediction == 2:
                st.error("🚨 High risk detected. Please consult a pediatrician if possible.")

            st.info("✅ This tool provides general tips. Always consult healthcare professionals for tailored advice.")

        except Exception as e:
            st.error(f"⚠️ An error occurred: {str(e)}")

# 🔁 Show page immediately
show_predictor()
