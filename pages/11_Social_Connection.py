import streamlit as st
import json, os, datetime as dt

st.set_page_config(page_title="Social Connection", page_icon="🤝")

st.title("🤝 Social Connection")
st.caption("Connect with other dashboard users, share updates, and support each other.")

# -----------------------------
# 1. Load subscription
# -----------------------------
if os.path.exists("subscription.json"):
    with open("subscription.json", "r") as f:
        active_plan = json.load(f).get("plan", "free")
else:
    active_plan = "free"

if active_plan == "free":
    st.warning("🔒 Upgrade to Standard or Premium to unlock Social Connections.")
    st.stop()

# -----------------------------
# 2. Community Feed (JSON file)
# -----------------------------
FEED_FILE = "community_feed.json"

if os.path.exists(FEED_FILE):
    with open(FEED_FILE, "r") as f:
        feed = json.load(f)
else:
    feed = []

# -----------------------------
# 3. Post an Update
# -----------------------------
st.subheader("✍️ Share Your Update")

username = st.text_input("Your Name (for community display):", "")
new_post = st.text_area("Write your update (e.g., health tip, progress, encouragement):")

if st.button("📢 Post to Community"):
    if username.strip() and new_post.strip():
        post = {
            "user": username.strip(),
            "text": new_post.strip(),
            "date": str(dt.date.today()),
            "likes": 0
        }
        feed.append(post)

        with open(FEED_FILE, "w") as f:
            json.dump(feed, f, indent=2)

        st.success("✅ Your post has been added to the community feed!")
    else:
        st.warning("Please enter your name and a message.")

st.divider()

# -----------------------------
# 4. Community Feed Display
# -----------------------------
st.subheader("🌍 Community Feed")

if not feed:
    st.info("No community posts yet. Be the first to share!")
else:
    for i, post in enumerate(reversed(feed[-10:])):  # show last 10
        st.write(f"**{post['user']}** ({post['date']}): {post['text']}")
        cols = st.columns([1, 4])
        with cols[0]:
            if st.button(f"👍 {post['likes']}", key=f"like_{i}"):
                feed[-(i+1)]["likes"] += 1
                with open(FEED_FILE, "w") as f:
                    json.dump(feed, f, indent=2)
                st.experimental_rerun()
        st.markdown("---")
