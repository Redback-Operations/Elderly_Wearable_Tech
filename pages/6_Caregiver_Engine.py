import streamlit as st
import pandas as pd
import plotly.express as px
import speech_recognition
import translate
import plotly
import pywaffle
import joblib


st.set_page_config(page_title="Caregiver Engine", page_icon="🧠")

def generate_recommendation(row):
    activity = row.get("physical_activity", 0)
    screen_time = row.get("screen_time", 0)
    snacks = row.get("snacking", "Unknown")

    recommendations = []

    if activity < 3:
        recommendations.append("🧍 Consider adding a short morning walk or chair yoga session.")
    elif activity < 6:
        recommendations.append("🚶 Keep up moderate movement—light stretching in the evening helps too.")
    else:
        recommendations.append("💪 Great job staying active! Keep it consistent.")

    if screen_time > 6:
        recommendations.append("📵 Try limiting screen time in the evenings and add screen breaks during the day.")
    elif screen_time > 3:
        recommendations.append("📺 Moderate screen use detected—add off-screen hobbies like reading or puzzles.")
    else:
        recommendations.append("🎯 Balanced screen time! Keep it up.")

    if "snacking" in row and isinstance(row["snacking"], str) and "sugary" in row["snacking"].lower():
        recommendations.append("🍎 Replace sugary snacks with fruits or nuts in the evening.")

    return " ".join(recommendations)

def show_caregiver_engine():
    st.header("🧠 Caregiver Recommendation Engine")
    st.markdown("""
    Upload a dataset to get personalized lifestyle suggestions based on activity and screen time.
    
    **Columns required**: `physical_activity`, `screen_time`
    """)

    uploaded_file = st.file_uploader("Upload CSV with at least 'physical_activity' and 'screen_time' columns", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("📊 Data Preview")
        st.dataframe(df.head())

        st.subheader("📈 Obesity Risk Distribution")
        if 'obesity_risk' in df.columns:
            chart = px.histogram(df, x='obesity_risk', color='obesity_risk', title='Obesity Risk Levels',
                                 category_orders={"obesity_risk": ["Low", "Medium", "High"]})
            st.plotly_chart(chart)

        st.subheader("📝 Recommendations")
        if 'physical_activity' in df.columns and 'screen_time' in df.columns:
            df_rec = df[['physical_activity', 'screen_time']].copy()
            df_rec['Caregiver_Advice'] = df.apply(generate_recommendation, axis=1)

            for i, row in df_rec.iterrows():
                with st.expander(f"Child #{i+1} Recommendation"):
                    st.write(f"**Physical Activity:** {row['physical_activity']}")
                    st.write(f"**Screen Time:** {row['screen_time']}")
                    st.markdown(f"**Advice:** {row['Caregiver_Advice']}")

            st.download_button("📥 Download CSV with Recommendations", data=df_rec.to_csv(index=False),
                               file_name="caregiver_recommendations.csv", mime="text/csv")

        # Optional: Link to Predictor output if available
        if 'obesity_risk' in df.columns:
            st.subheader("🤝 Linked with Risk Prediction")
            st.markdown("This engine complements the Predictor module. Use the predicted 'obesity_risk' to inform lifestyle guidance.")

# Show page immediately
show_caregiver_engine()
