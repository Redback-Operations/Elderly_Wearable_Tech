# pages/1_Home.py
import speech_recognition
import translate
import plotly
import pywaffle
import joblib
import streamlit as st
import base64

# Translation helper
def _(text):
    return st.session_state["translator"].translate(text)

st.set_page_config(page_title="Home", page_icon="🏠")

# Optional: Function to play local audio guide
def play_audio(file_path):
    try:
        with open(file_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            audio_base64 = base64.b64encode(audio_bytes).decode()
            audio_html = f"""
                <audio controls autoplay>
                    <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                    Your browser does not support the audio element.
                </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(_("Audio guide not found. Please add 'help_guide.mp3' to the assets folder."))

def show_home():
    st.title(_("🏠 CHILDHOOD OBESITY RISK DASHBOARD"))
    st.caption(_("SUPPORTING HEALTHIER ROUTINES FOR CHILDREN AND CAREGIVERS"))

    st.markdown("---")

    st.subheader(_("WHO IS THIS FOR?"))
    st.markdown(_("""
    Designed for **caregivers, health workers, and families** to:

    - Spot early obesity risks  
    - Support healthier sleep and meals  
    - Start meaningful health conversations
    """))

    st.markdown("---")

    with st.expander(_("WHY OBESITY RISK MATTERS"), expanded=False):
        st.markdown(_("""
        Childhood obesity is more than just weight. It affects:

        - Mood and energy  
        - Sleep quality  
        - Long-term health outcomes

        > Prevention starts with awareness — and you, the caregiver, make that possible.
        """))

    with st.expander(_("HOW TO USE THIS DASHBOARD"), expanded=False):
        st.markdown(_("""
        1. Upload or explore a dataset  
        2. Run the prediction tool  
        3. View insights from lifestyle patterns  
        4. Review fairness and ethical safeguards
        """))

    with st.expander(_("ELDERLY + WEARABLES IN PREVENTION"), expanded=False):
        st.markdown(_("""
        Senior caregivers using smartwatches or bands can help by:

        - Tracking children's activity  
        - Monitoring sleep during overnight care  
        - Reducing prolonged screen exposure

        Wearable monitoring bridges child health and elderly caregiving — a shared path to well-being.
        """))

    with st.expander(_("NEED HELP? EMERGENCY GUIDE"), expanded=False):
        st.markdown(_("### Quick Walkthrough"))

        st.markdown(_("""
        - **Home Tab:** Learn who this dashboard is for and its purpose.  
        - **Data Explorer:** Upload a CSV and explore lifestyle data.  
        - **Predictor:** Run obesity risk predictions.  
        - **Caregiver Engine:** View practical tips tailored to each child.  
        - **Privacy Tab:** Export data locally, delete session memory.  
        - **Fairness Tab:** Understand how ethical design protects users.
        """))

        st.markdown(_("Tip: Ask someone to assist if you need help uploading files or navigating tabs."))

        if st.checkbox(_("Play Audio Help Guide")):
            play_audio("assets/help_guide.mp3")  # Ensure this file exists

    st.markdown("---")

    st.subheader(_("DISCLAIMER"))
    st.info(_("""
    This is an educational prototype.  
    It does not collect personal data or offer medical advice.  
    Always consult healthcare professionals for real-world health support.
    """))

# Display the Home page
show_home()
