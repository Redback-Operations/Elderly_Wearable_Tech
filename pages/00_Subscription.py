import streamlit as st
import json, os

st.set_page_config(page_title="Subscription Plans", page_icon="💳")

st.title("💳 Subscription Plans")
st.caption("Choose a plan that works best for you or your family.")

# -----------------------------
# 1. Subscription Plans
# -----------------------------
plans = {
    "free": {
        "name": "Free Plan",
        "price": "$0 / week",
        "features": [
            "✅ Track personal streaks (Activity, Sleep, Memory Aids)",
            "✅ Daily habit reminders",
            "❌ No social or family sharing"
        ]
    },
    "standard": {
        "name": "Standard Plan",
        "price": "$20.99 / week",
        "features": [
            "✅ Track streaks (Activity, Sleep, Memory Aids)",
            "✅ Social Sharing with community",
            "✅ Connect with other dashboard users",
            "❌ No family sharing features"
        ]
    },
    "premium": {
        "name": "Premium Plan",
        "price": "$79.99 / week",
        "features": [
            "✅ Everything in Free + Standard",
            "✅ Family Sharing Portal",
            "✅ Family Support & Messaging",
            "✅ Social Connections",
            "✅ Weekly Reports & Alerts",
            "✅ Caregiver monitoring"
        ]
    }
}

# -----------------------------
# 2. Display Plan Options
# -----------------------------
cols = st.columns(3)

for i, key in enumerate(plans.keys()):
    plan = plans[key]
    with cols[i]:
        st.subheader(plan["name"])
        st.metric("Price", plan["price"])
        for f in plan["features"]:
            st.write(f)
        if st.button(f"Subscribe to {plan['name']}", key=key):
            st.session_state["active_plan"] = key
            st.success(f"✅ You have subscribed to {plan['name']}")

# -----------------------------
# 3. Persist Subscription Choice
# -----------------------------
FILE = "subscription.json"

if "active_plan" not in st.session_state:
    # Load from file if exists
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)
            st.session_state["active_plan"] = data.get("plan", "free")
    else:
        st.session_state["active_plan"] = "free"

# Save selection when changed
if "active_plan" in st.session_state:
    with open(FILE, "w") as f:
        json.dump({"plan": st.session_state["active_plan"]}, f)

st.info(f"Your current plan: **{plans[st.session_state['active_plan']]['name']}**")

