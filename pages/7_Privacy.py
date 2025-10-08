# pages/7_Privacy.py

import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
import speech_recognition
import translate
import plotly
import pywaffle
import joblib


st.set_page_config(page_title="Privacy & Data Control", page_icon="🔐")

# Function to clear session data
def clear_session_data():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

# Function to generate PDF report with logo and timestamp
def generate_pdf(dataframe):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    flowables = []

    # Add Deakin or custom project logo
    logo_path = "data/deakin_logo.png"  # Ensure this path is correct
    try:
        flowables.append(Image(logo_path, width=150, height=60))
    except Exception as e:
        flowables.append(Paragraph("(Logo could not be loaded)", styles['Normal']))

    flowables.append(Paragraph("Childhood Obesity Dashboard – Data Snapshot", styles['Title']))
    flowables.append(Paragraph("This is a locally generated summary. No cloud data storage is involved.", styles['Normal']))
    
    df_str = dataframe.to_string(index=False)
    for line in df_str.split('\n'):
        flowables.append(Paragraph(line, styles['Code']))

    doc.build(flowables)
    buffer.seek(0)
    return buffer

# Main display function
def show_privacy_page():
    st.header("Privacy-First Design")
    st.markdown("""
    This dashboard follows strict privacy practices tailored for elderly caregivers:

    - No personal data is stored online or sent to external servers.
    - All user data is stored temporarily in session memory only.
    - You can export your data to a PDF file for offline use.
    - You can delete your data from memory at any time.
    """)

    st.caption("Upload a CSV file to preview privacy features")

    uploaded_file = st.file_uploader("📁 Upload CSV", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.session_state['local_data'] = df

        st.success("✅ Data stored locally in this session only.")
        st.dataframe(df)

        # Export to timestamped PDF
        if st.button("📄 Export to PDF"):
            pdf_file = generate_pdf(df)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"data_summary_{timestamp}.pdf"
            st.download_button(
                label="⬇️ Download PDF",
                data=pdf_file,
                file_name=filename,
                mime="application/pdf"
            )

        # Clear session data
        if st.button("🧹 Delete Session Data"):
            clear_session_data()
            st.warning("Session data deleted. Please refresh to confirm.")

    else:
        st.info("ℹ️ Upload a file to preview privacy features.")

# Show page
show_privacy_page()
