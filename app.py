# app.py

import streamlit as st
from utils.translator import get_translator
import os

# -----------------------------
# Configure app layout 
# -----------------------------
st.set_page_config(
    page_title="Childhood Obesity Risk Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Translator setup (default English)
# -----------------------------
if 'translator' not in st.session_state:
    st.session_state['translator'] = get_translator('en')  # default language

# Language selector
lang = st.selectbox(
    "🌐 Select Language",
    ['English', 'Italiano', 'Ελληνικά', '中文'],
    key="language_select"
)

if lang == 'English':
    st.session_state['translator'] = get_translator('en')
elif lang == 'Italiano':
    st.session_state['translator'] = get_translator('it')
elif lang == 'Ελληνικά':
    st.session_state['translator'] = get_translator('el')
elif lang == '中文':
    st.session_state['translator'] = get_translator('zh-cn')

_ = st.session_state['translator'].translate

# -----------------------------
# Homepage content
# -----------------------------
st.title(_("🏠 Welcome to the Childhood Obesity Risk Dashboard"))

st.markdown(_("""
This dashboard uses publicly available Australian health data to predict childhood obesity risk 
based on lifestyle and demographic factors.  

Navigate using the sidebar to explore key features:
- 📊 Data Explorer
- ⚖️ Fairness & Ethics
- 🔍 Insights
- 🎯 Predictor
- 🧑‍🤝‍🧑 Caregiver Engine
- 🔒 Privacy
- 🎮 Healthy Habits Streaks (NEW!)
- 📍 Resource Hub

**Note:** This is an educational prototype — no personal data is collected or stored.
"""))

st.info(_("Tip: Start with the Predictor or Healthy Habits Streaks to try out the core features."))

# -----------------------------
# Sidebar navigation
# -----------------------------
with st.sidebar:
    st.header("Go to pages")
    st.page_link("pages/5_Predictor.py", label="🎯 Predictor")
    st.page_link("pages/7_Resource_Hub.py", label="📍 Resource Hub")
    if os.path.exists("pages/08_Healthy_Habits_Streaks.py"):
        st.page_link("pages/08_Healthy_Habits_Streaks.py", label="🎮 Healthy Habits Streaks")
    else:
        st.caption("⚠️ Streaks page not found. Expected: pages/08_Healthy_Habits_Streaks.py")
