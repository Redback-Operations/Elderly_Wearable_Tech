import streamlit as st

st.title("🔥 Overall Streak Summary")

st.write("Here’s how you’re doing across all lifestyle habits:")

st.metric("Memory Aids Streak", st.session_state.get("memory_streak", 0))
st.metric("Sleep Streak", st.session_state.get("sleep_streak", 0))
st.metric("Healthy Habits Streak (from page 08)", st.session_state.get("healthy_streak", 0))
