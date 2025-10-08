# pages/4_Insights.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle
import speech_recognition
import translate
import plotly
import pywaffle
import joblib


st.set_page_config(page_title="Insights", page_icon="📈")

def show_insights():
    st.header("📈 Key Insights & Proportions")

    uploaded_file = st.file_uploader("Upload processed dataset (CSV)", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("✅ **Dataset Preview:**", df.head())

        # ===============================
        # 🔷 1. Icon Array – Waffle Chart
        # ===============================
        if 'obesity_risk' not in df.columns:
            st.error("❌ 'obesity_risk' column not found in the dataset.")
            return

        risk_counts = df['obesity_risk'].value_counts()
        categories = {str(k): v for k, v in risk_counts.items()}

        st.markdown("### 🧱 Icon Array: Childhood Obesity Risk Distribution")

        fig1 = plt.figure(
            FigureClass=Waffle,
            rows=5,
            values=categories,
            colors=["#4CAF50", "#FFC107", "#F44336"],  # Green, Yellow, Red
            icons='child',
            icon_size=25,
            icon_legend=True,
            legend={'loc': 'upper left', 'bbox_to_anchor': (1.05, 1)}
        )
        st.pyplot(fig1)

        st.caption("""
        🧠 **Why this chart?**  
        Icon arrays (waffle charts) use human-friendly icons to show proportions.  
        Each 👧 represents a child, making it easy to see how many are at risk.
        """)

        # ===============================
        # 🔷 2. Line Chart – Time Trends
        # ===============================
        st.markdown("### 📉 Time Trend: Screen Time / Activity Over Weeks")

        time_candidates = [col for col in df.columns if 'week' in col.lower() or 'date' in col.lower()]
        if not time_candidates:
            st.warning("⚠️ No date or week column found. Please upload data with a time column.")
        else:
            time_column = st.selectbox("🗓️ Select Time Column", time_candidates)
            y_column = st.selectbox("📈 Select Variable to Trend", ['screen_time', 'physical_activity'])

            if time_column in df.columns and y_column in df.columns:
                df_sorted = df.sort_values(by=time_column)
                fig2, ax = plt.subplots()
                ax.plot(df_sorted[time_column], df_sorted[y_column], marker='o', color="#FB5607")
                ax.set_xlabel(time_column.replace('_', ' ').title())
                ax.set_ylabel(y_column.replace('_', ' ').title())
                ax.set_title(f"{y_column.replace('_', ' ').title()} Over Time")
                ax.grid(True)
                st.pyplot(fig2)

                st.caption("""
                🧠 **Why this chart?**  
                Simple line charts help elderly caregivers spot trends — like increasing screen time or decreasing activity — with clear markers.
                """)

# 🔁 Show page immediately
show_insights()
