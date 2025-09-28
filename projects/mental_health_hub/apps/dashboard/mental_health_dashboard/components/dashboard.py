import streamlit as st
import plotly.graph_objects as go

def mood_summary(latest, df, mood_color):
    st.markdown("### 📈 Mood Score Overview")
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=latest["MoodScore"],
        delta={'reference': df["MoodScore"].iloc[-2]},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': mood_color},
            'steps': [
                {'range': [0, 65], 'color': "#EF9A9A"},
                {'range': [65, 75], 'color': "#FFF9C4"},
                {'range': [75, 100], 'color': "#A2D5AB"}
            ]
        }
    ))
    st.plotly_chart(fig, use_container_width=True)
