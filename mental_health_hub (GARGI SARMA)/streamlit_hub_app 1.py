# Import all necessary libraries and functions here
import streamlit as st
from auth_module import run_auth
from dashboard_module import run_dashboard
from mood_module import run_mood
from logging_module import run_logging, init_logging  
from storytelling_module import run_storytelling   # ⬅️ NEW
from chat_module import run_chat

# Page Directory for Streamlit
PAGES = {
    "Authentication": run_auth,       # Add Authentication Page
    "Dashboard": run_dashboard,       # Add Dashboard page
    "Mood Predictor": run_mood,       # Add Mood Predictor Page
    "Activity Logging": run_logging,  # Add Logging page 
    "Storytelling": run_storytelling, # Add Storytelling Page
    "Group Chat": run_chat,         # Add Group Chat Page
}

# Initialises logging session when the app starts
init_logging()  

# Main Functionality
def main():
    st.sidebar.title("Mental Health Hub")
    choice = st.sidebar.radio("Go to:", list(PAGES.keys()))
    PAGES[choice]()  # run the selected page

if __name__ == "__main__":
    main()
