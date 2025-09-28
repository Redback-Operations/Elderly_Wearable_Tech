import datetime
import json
import streamlit as st
import pandas as pd  

# Session Initialization 
def init_logging():
    if 'logs' not in st.session_state:
        st.session_state.logs = []

# Initialize session state
init_logging()

# Logging Functionality
def log_event(action, severity='INFO', details=None):
    """Log only significant events like login, registration, etc."""
    entry = {
        'timestamp': datetime.datetime.utcnow().isoformat() + 'Z',
        'action': action,
        'severity': severity,
        'details': details
    }
    st.session_state.logs.append(entry)

# Run the logging page
def run_logging():
    st.title("Activity Logs")

    # Check if there are any logs in session
    logs = st.session_state.logs

    # Display the logs in a table format using st.dataframe
    if logs:
        severity_filter = st.selectbox('Filter by severity', ['ALL', 'INFO', 'WARNING', 'ERROR'])
        filtered_logs = logs[::-1]  # latest first
        
        # Apply filter if selected
        if severity_filter != 'ALL':
            filtered_logs = [log for log in filtered_logs if log['severity'] == severity_filter]

        # Display logs in a table format
        st.dataframe(pd.DataFrame(filtered_logs))  # Display logs as a dataframe

        # Add export functionality
        if st.button("Export Logs as JSON"):
            logs_json = json.dumps(filtered_logs, indent=2)
            st.download_button(label="Download JSON", data=logs_json, file_name="logs.json", mime="application/json")
    else:
        st.info("No logs to display yet.")
