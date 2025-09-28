import streamlit as st
import plotly.express as px

def mood_trend_chart(df):
    st.subheader("📈 Monthly Mood Score Trends")
    fig = px.line(df, x="Date", y="MoodScore", markers=True, title="Mood Score Over Time")
    fig.update_layout(
        yaxis_title="Mood Score",
        xaxis_title="Date",
        height=500,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)
