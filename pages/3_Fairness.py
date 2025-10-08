# pages/5_Fairness.py

import streamlit as st
import speech_recognition
import translate
import plotly
import pywaffle
import joblib


st.set_page_config(page_title="Fairness", page_icon="⚖️")

def show_fairness():
    st.header("⚖️ FAIRNESS & ETHICS")
    st.markdown("---")

    st.markdown("## 🛡️ 1. PRIVACY, SECURITY & DATA ETHICS")
    st.markdown("""
    - **Privacy by Design**: This app does not collect any real-time personal data. Data minimisation is built-in.
    - **Clear Consent & Control**: Only essential information is requested, and all data remains local on your device.
    - **Minimal Risk Operation**: Undo and reset options are visible where available. The UI avoids hidden actions or confusing flows.
    """)

    st.markdown("## 📣 2. VOICE & PARTICIPATION: RESPECT THROUGH CO-DESIGN")
    st.markdown("""
    - **Participatory Design**: Older adults and caregivers contributed feedback to improve usability.
    - **Respectful Language**: Clear, non-patronising labels and microcopy support dignity and understanding.
    - **Polite, Efficient Interactions**: Layouts are decluttered, with simple instructions and minimal steps to reduce cognitive load.
    """)

    st.markdown("## ♿ 3. INCLUSIVE DESIGN THAT REDUCES EXCLUSION")
    st.markdown("""
    - **Universal Design**: The dashboard uses high contrast, large fonts, and clear buttons to suit users with varying needs.
    - **Accessibility Compliance**: The layout follows WCAG guidelines—scalable text, tap-friendly elements, and keyboard navigation.
    - **No Special Modes**: The experience is consistent for all users without separate “senior” settings.
    """)

    st.markdown("## 💬 4. FAIRNESS & ETHICAL TRANSPARENCY")
    st.markdown("""
    - **Equitable Feature Access**: Any feature (like font size or color adjustments) works equally well across views.
    - **Clear System Feedback**: Visual updates, button highlights, and messages confirm user actions.
    - **Bias Prevention**: Models are evaluated for fairness (e.g., demographic parity), and PCA reduces hidden bias.
    - **No Assumptions**: The design avoids stereotypes about tech skills, offering autonomy without oversimplification.
    """)

    st.markdown("## 🎓 NOTE")
    st.markdown("""
    All outputs are **simulated for educational purposes only**. This tool is not intended for medical decision-making.
    """)

show_fairness()
