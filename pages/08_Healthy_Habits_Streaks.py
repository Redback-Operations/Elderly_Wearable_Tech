import streamlit as st
import datetime as dt
import json, os

st.title("🎮 Healthy Habits Streaks")

# --------------------------
# Step 1: Setup JSON persistence
# --------------------------
FILE = "streaks.json"

# Load streaks from file if exists
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        streaks = json.load(f)
else:
    streaks = {
        "screen_time_ok": 0,
        "activity_done": 0,
        "sleep_ok": 0,
        "memory_ok": 0,
        "last_date": None,
        "logged_today": [],
    }

# Put into session_state
if "streaks" not in st.session_state:
    st.session_state.streaks = streaks

today = dt.date.today()
last_date = (
    dt.date.fromisoformat(st.session_state.streaks["last_date"])
    if st.session_state.streaks["last_date"]
    else None
)

# --------------------------
# Step 2: Reset if day skipped
# --------------------------
if last_date and (today - last_date).days > 1:
    for k in ("screen_time_ok", "activity_done", "sleep_ok", "memory_ok"):
        st.session_state.streaks[k] = 0
    st.session_state.streaks["logged_today"] = []

# --------------------------
# Step 3: Habit logging
# --------------------------
col1, col2, col3 = st.columns(3)

# Screen time
with col1:
    st.subheader("📱 Screen time")
    ok = st.toggle("≤ 2 hrs today?", key="screen_time")
    if ok and "screen_time_ok" not in st.session_state.streaks["logged_today"]:
        st.session_state.streaks["screen_time_ok"] += 1
        st.session_state.streaks["logged_today"].append("screen_time_ok")
        st.session_state.streaks["last_date"] = str(today)
        with open(FILE, "w") as f:
            json.dump(st.session_state.streaks, f)

# Activity
with col2:
    st.subheader("🏃 Activity")
    done = st.toggle("≥ 60 mins activity?", key="activity")
    if done and "activity_done" not in st.session_state.streaks["logged_today"]:
        st.session_state.streaks["activity_done"] += 1
        st.session_state.streaks["logged_today"].append("activity_done")
        st.session_state.streaks["last_date"] = str(today)
        with open(FILE, "w") as f:
            json.dump(st.session_state.streaks, f)

# Sleep
with col3:
    st.subheader("🛌 Sleep")
    good = st.toggle("7–9 hrs sleep?", key="sleep")
    if good and "sleep_ok" not in st.session_state.streaks["logged_today"]:
        st.session_state.streaks["sleep_ok"] += 1
        st.session_state.streaks["logged_today"].append("sleep_ok")
        st.session_state.streaks["last_date"] = str(today)
        with open(FILE, "w") as f:
            json.dump(st.session_state.streaks, f)

st.divider()

# --------------------------
# Step 4: Metrics
# --------------------------
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Screen-time streak", st.session_state.streaks["screen_time_ok"])
with c2:
    st.metric("Activity streak", st.session_state.streaks["activity_done"])
with c3:
    st.metric("Sleep streak", st.session_state.streaks["sleep_ok"])
with c4:
    st.metric("Memory streak", st.session_state.streaks["memory_ok"])

st.info("Tip: streaks reset if you miss a day. Each habit only counts once per day.")

# --------------------------
# Step 5: Memory Aids
# --------------------------
st.header("📝 Memory Aids")

reminders = [
    "Don’t forget your morning walk 🏃",
    "Drink a glass of water 💧 now",
    "Stretch for 5 minutes 🙆",
]

today_idx = today.day % len(reminders)
st.info(reminders[today_idx])

if st.button("✅ I did it! (Memory Aid)") and "memory_ok" not in st.session_state.streaks["logged_today"]:
    st.session_state.streaks["memory_ok"] += 1
    st.session_state.streaks["logged_today"].append("memory_ok")
    st.session_state.streaks["last_date"] = str(today)
    with open(FILE, "w") as f:
        json.dump(st.session_state.streaks, f)
    st.success(f"Great job! Your memory streak is now {st.session_state.streaks['memory_ok']} 🔥")
