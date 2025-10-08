import streamlit as st
import pandas as pd
import plotly.express as px
import speech_recognition
import translate
import plotly
import pywaffle
import joblib


# Page configuration
st.set_page_config(page_title="Data Explorer", page_icon="📂", layout="wide")

# Styling for elderly users (large fonts and bold labels)
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-size: 20px !important;
        }
        .stSelectbox label, .stFileUploader label {
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

def show_data_explorer():
    st.markdown("## 🗂️ Data Explorer")
    st.markdown("Upload a **CSV file** with lifestyle or health-related data (e.g., LSAC/ABS datasets).")

    uploaded_file = st.file_uploader("📁 Drag and drop or browse your file here", type="csv")

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            st.error(f"❌ Failed to read CSV file: {e}")
            return

        st.success("✅ Preview of Your Dataset")
        st.dataframe(df.head(), use_container_width=True)

        column = st.selectbox("🔍 Select a column to explore", df.columns)

        if df[column].dtype == 'object' or df[column].nunique() <= 20:
            st.markdown("### 📊 Value Counts Bar Chart")
            value_counts = df[column].value_counts().reset_index()
            value_counts.columns = [column, 'Count']

            fig = px.bar(
                value_counts,
                x='Count',
                y=column,
                orientation='h',
                color='Count',
                color_continuous_scale='Blues',
                labels={column: column.replace('_', ' ').title(), 'Count': 'Number of Entries'},
                title=f"Distribution of {column.replace('_', ' ').title()}"
            )
            fig.update_layout(
                height=500,
                xaxis_title="Number of Entries",
                yaxis_title=column.replace('_', ' ').title(),
                font=dict(size=18),
            )
            st.plotly_chart(fig, use_container_width=True)

            st.info("🧠 **Tip:** Interactive bar charts help older adults understand and explore data more easily.")
        else:
            st.warning("⚠️ Please select a column with categorical or limited unique values (not continuous).")

# Run the explorer
show_data_explorer()

st.markdown("""
🧾 **What does "Number of Entries" mean?**

This tells you how many times each category appears in the data.
For example, if “High Screen Time” shows 12 entries, it means 12 children had high screen time.
""")

