import streamlit as st
from utils.data_loader import load_data
from utils.mood_logic import get_mood_zone
from components.dashboard import mood_summary
from components.mood_chart import mood_trend_chart
from components.support_mindfulness import support_section, mindfulness_gif
from components.chatbot import chatbot_box
from components.game_mind_match import play_mind_match

# --- CONFIG ---
st.set_page_config(page_title="ElderCare Wellness", layout="wide")

st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
        font-family: 'Segoe UI', sans-serif;
        font-size: 18px;
    }
    h1, h2, h3, h4 {
        color: #2E4A62;
    }
    .stButton>button {
        background-color: #6c8caf;
        color: white;
        font-size: 18px;
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)

# --- LOAD DATA ---
df = load_data()
latest = df.iloc[-1]
zone = get_mood_zone(latest["MoodScore"])

# --- COLOR MAP ---
MOOD_COLORS = {
    "good": "#A2D5AB",
    "moderate": "#FFF9C4",
    "low": "#EF9A9A"
}
mood_color = MOOD_COLORS[zone]

# --- HEADER ---
st.markdown("## <b>ElderCare Mental Wellness Dashboard</b>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

# --- MOOD GAUGE ---
with col1:
    mood_summary(latest, df, mood_color)

# --- DAILY METRICS ---
with col2:
    st.markdown("""
    <div style='padding: 20px; border: 1px solid #ddd; border-radius: 10px; background-color: #ffffff'>
    <h4>🛌️ Sleep & Movement</h4>
    </div>
    """, unsafe_allow_html=True)
    st.metric("Sleep (hrs)", f"{latest['SleepHours']} hrs")
    st.metric("Movement Score", f"{latest['MovementScore']} pts")
    st.metric("Medication", "✅ Taken" if latest["MedicationTaken"] == 1 else "⚠️ Missed")

# --- WELLNESS TIP ---
st.markdown("---")
st.subheader("🌞 Daily Wellness Tip")
if latest["SleepHours"] < 6.5:
    st.info("Try to get at least 7 hours of sleep. Good rest improves mood!")
elif latest["MovementScore"] < 40:
    st.info("A short walk or gentle stretch may help lift your energy.")
else:
    st.success("You're doing well today! Keep it up.")

# --- TRENDS ---
st.markdown("---")
mood_trend_chart(df)

# --- SUPPORT & MINDFULNESS ---
st.markdown("---")
st.subheader("🪘 Support & Mindfulness")
col3, col4 = st.columns(2)
with col3:
    support_section()
with col4:
    mindfulness_gif()

# --- CHATBOT ---
chatbot_box(latest["MoodScore"])

# --- SECTION 6: GAME ---
st.markdown("---")
play_mind_match()

from sections.support_and_mindfulness import mindfulness_gif, support_section

# Inside the layout section
col3, col4 = st.columns(2)
with col3:
    support_section()
with col4:
    mindfulness_gif()
