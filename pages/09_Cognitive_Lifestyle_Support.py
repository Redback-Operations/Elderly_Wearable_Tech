import streamlit as st
import datetime
import time

st.set_page_config(page_title="Cognitive & Lifestyle Support", page_icon="🧠")

st.title("🧠 Cognitive & Lifestyle Support")
st.markdown("Tools to support memory, lifestyle habits, and relaxation — designed for both children & elders.")

# Initialize streaks in session_state
if "memory_streak" not in st.session_state:
    st.session_state.memory_streak = 0
if "sleep_streak" not in st.session_state:
    st.session_state.sleep_streak = 0

today = datetime.date.today()

# -------------------------
# Section 1: Memory Aids
# -------------------------
st.header("📝 Memory Aids")

reminders = [
    "Don’t forget your morning walk 🏃",
    "Drink a glass of water 💧 now",
    "Stretch for 5 minutes 🙆",
    "Call a friend or family member ☎️",
    "Do a quick brain puzzle 🧩"
]

today_idx = today.day % len(reminders)
st.info(reminders[today_idx])

if st.button("✅ I did it! (Memory Aid)"):
    st.session_state.memory_streak += 1
    st.success(f"Great job! Your memory streak is now {st.session_state.memory_streak} 🔥")

st.metric("Memory Streak", st.session_state.memory_streak)

st.divider()

# -------------------------
# Section 2: Educational Tips
# -------------------------
st.header("📘 Daily Health Tip")

tips = [
    "Stretch while watching TV 📺",
    "Choose fruit instead of sugary snacks 🍎",
    "Go for a 10-min walk after meals 🚶",
    "Keep a water bottle nearby 💧",
    "Practice gratitude before bed 🙏",
    "Limit caffeine in the evening ☕"
]

today_tip = tips[today.day % len(tips)]
st.success(today_tip)

st.divider()

# -------------------------
# Section 3: Relaxation Guide
# -------------------------
st.header("🌙 Relaxation & Sleep Tracking")

st.markdown("Follow a simple breathing exercise to relax:")

if st.button("Start Breathing Exercise"):
    for i in range(3):
        st.write("🌬️ Breathe in...")
        time.sleep(3)
        st.write("😌 Hold...")
        time.sleep(2)
        st.write("🎈 Breathe out...")
        time.sleep(4)
    st.success("Well done! Feeling calmer already 😌")

# Sleep logging
sleep_hours = st.slider("How many hours did you sleep last night?", 0, 12, 7)
st.write(f"You logged **{sleep_hours} hours** of sleep 😴")

if sleep_hours >= 7:
    if st.button("✅ Mark Sleep as Healthy"):
        st.session_state.sleep_streak += 1
        st.success(f"Awesome! Your sleep streak is {st.session_state.sleep_streak} 🌟")
else:
    st.warning("Try to get at least 7–8 hours for better health 💡")

st.metric("Sleep Streak", st.session_state.sleep_streak)

st.divider()

# -------------------------
# Section 4: Quick Tips Panel
# -------------------------
st.header("💡 Quick Lifestyle Reminders")
st.write("- Stay hydrated 💧")
st.write("- Move every hour 🕒")
st.write("- Keep a consistent bedtime 🛌")
st.write("- Connect socially with friends/family 🤝")
