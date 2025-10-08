import streamlit as st
import json, os, datetime as dt, random

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="Family Support", page_icon="🌍")
st.title("🌍 Family Support Portal")
st.caption("View loved one’s progress and send encouragement messages.")

# -----------------------------
# PIN setup (safe fallback)
# -----------------------------
DEFAULT_PIN = "1234"  # fallback PIN

try:
    PIN = st.secrets["portal_pin"]  # read from secrets.toml
except Exception:
    PIN = DEFAULT_PIN               # fallback if not found

with st.expander("🔒 Family Access"):
    entered = st.text_input("Enter family PIN", type="password")
    st.caption("Tip: set a secure PIN in `.streamlit/secrets.toml` like:\n\nportal_pin = \"your-pin\"")

if entered != PIN:
    st.info("Enter the PIN to view family support features.")
    st.stop()

# -----------------------------
# Helper loaders
# -----------------------------
def load_json(path, default):
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except Exception:
            return default
    return default

# File paths
STREAKS_FILE     = "streaks.json"
WEEKLY_FILE      = "weekly_report.json"
DIARY_FILE       = "diary.json"
NOTES_FILE       = "family_messages.json"        # elder → family
ENCOURAGE_FILE   = "family_encouragement.json"   # family → elder

# Load data
streaks = load_json(STREAKS_FILE, {
    "screen_time_ok": 0, "activity_done": 0,
    "sleep_ok": 0, "memory_ok": 0, "last_date": None
})
weekly  = load_json(WEEKLY_FILE, {"date": None, "report": "No weekly report saved yet."})
diary   = load_json(DIARY_FILE, [])
notes   = load_json(NOTES_FILE, [])
encs    = load_json(ENCOURAGE_FILE, [])

today = dt.date.today()

# -----------------------------
# Subscription gate
# -----------------------------
if os.path.exists("subscription.json"):
    with open("subscription.json", "r") as f:
        active_plan = json.load(f).get("plan", "free")
else:
    active_plan = "free"

if active_plan == "free":
    st.warning("🔒 Upgrade to Standard or Premium to unlock Family Support features.")
    st.stop()
elif active_plan == "standard":
    st.success("✅ You are on Standard Plan (basic social features).")
    st.stop()
elif active_plan == "premium":
    st.success("🌟 You are on Premium Plan (all family support features unlocked).")

st.divider()

# -----------------------------
# Alerts / Safety signals
# -----------------------------
days_since_log = None
if streaks.get("last_date"):
    try:
        last_dt = dt.date.fromisoformat(streaks["last_date"])
        days_since_log = (today - last_dt).days
    except Exception:
        days_since_log = None

alert_msgs = []
if days_since_log is None:
    alert_msgs.append("No last activity date available yet.")
else:
    if days_since_log >= 3:
        alert_msgs.append(f"⚠️ No new habit logs for **{days_since_log} days**.")
    elif days_since_log == 2:
        alert_msgs.append("⚠️ No new habit logs for **2 days** (please check in).")

if streaks.get("sleep_ok", 0) == 0:
    alert_msgs.append("ℹ️ Sleep streak is at 0 days.")

st.subheader("👀 Current Status")
if alert_msgs:
    for a in alert_msgs:
        st.warning(a)
else:
    st.success("✅ All good—recent activity detected.")

st.divider()

# -----------------------------
# Streak summary
# -----------------------------
st.subheader("📊 Streak Summary")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Activity streak", streaks.get("activity_done", 0))
c2.metric("Sleep streak", streaks.get("sleep_ok", 0))
c3.metric("Memory aids",  streaks.get("memory_ok", 0))
c4.metric("Screen-time OK", streaks.get("screen_time_ok", 0))

last_str = streaks.get("last_date") or "—"
st.caption(f"Last habit log date: **{last_str}**")

summary_text = (
    f"Health update ({today.isoformat()}):\n"
    f"- Activity streak: {streaks.get('activity_done',0)} days\n"
    f"- Sleep streak: {streaks.get('sleep_ok',0)} days\n"
    f"- Memory aids streak: {streaks.get('memory_ok',0)} days\n"
    f"- Screen-time OK streak: {streaks.get('screen_time_ok',0)} days\n"
    f"Last habit log date: {last_str}"
)
st.download_button("⬇️ Download summary (txt)", summary_text, file_name="family_summary.txt", mime="text/plain")

st.divider()

# -----------------------------
# Weekly report
# -----------------------------
st.subheader("🗓️ Weekly Report")
st.write(weekly.get("report", "No weekly report saved yet."))
st.caption(f"Report date: {weekly.get('date') or '—'}")

wr_text = f"Date: {weekly.get('date')}\n\n{weekly.get('report','')}"
st.download_button("⬇️ Download weekly report (txt)", wr_text, file_name="weekly_report.txt", mime="text/plain")

st.divider()

# -----------------------------
# Diary (last 5 entries)
# -----------------------------
st.subheader("📖 Recent Diary Notes")
if diary:
    for entry in reversed(diary[-5:]):
        st.write(f"**{entry.get('date','—')}** — {entry.get('text','')}")
else:
    st.info("No diary notes yet.")

st.divider()

# -----------------------------
# Elder → family notes
# -----------------------------
st.subheader("💌 Messages from Elder")
if notes:
    for m in reversed(notes[-5:]):
        st.write(f"**{m.get('date','—')}** — {m.get('text','')}")
else:
    st.info("No saved messages yet.")

st.divider()

# -----------------------------
# Family → elder encouragement (display)
# -----------------------------
st.subheader("🌟 Family Encouragement")
if encs:
    for e in reversed(encs[-5:]):  # show last 5
        if isinstance(e, dict):
            st.success(f"💌 {e.get('from','Family')} ({e.get('date','—')}): {e.get('text','')}")
        else:
            st.success(f"💌 {e}")  # legacy string-only format
else:
    st.info("No encouragement messages yet.")

st.divider()

# -----------------------------
# Family → elder encouragement (write new)
# -----------------------------
st.subheader("✍️ Write a Message to Your Loved One")
sender = st.text_input("Your Name (Family Member):", "")
new_msg = st.text_area("Type your encouragement:")

if st.button("📨 Send Message"):
    if sender.strip() and new_msg.strip():
        msg = {"from": sender.strip(), "text": new_msg.strip(), "date": str(dt.date.today())}

        if os.path.exists(ENCOURAGE_FILE):
            with open(ENCOURAGE_FILE, "r") as f:
                encs = json.load(f)
        else:
            encs = []

        encs.append(msg)

        with open(ENCOURAGE_FILE, "w") as f:
            json.dump(encs, f, indent=2)

        st.success("✅ Your message has been saved and will appear in elder’s dashboard.")
    else:
        st.warning("Please enter your name and a message.")
