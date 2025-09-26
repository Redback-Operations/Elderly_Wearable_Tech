# Streamlit Hub Application

## Overview
This module integrates all individual features into a single cohesive demo platform using Streamlit.
It acts as the central hub for authentication, logging, mental health dashboard, mood prediction, and collaborative storytelling.


## Files in this module

- **streamlit_hub_app.py** → Main entry point that ties everything together into a navigable multi-page app.
- **auth_module.py** → Implements user registration, login, logout with JWT authentication.
- **logging_module.py** → Centralised event logging with severity levels.
- **dashboard_module.py** → Data generation and visualisations for mental health trends.
- **mood_module.py** → Simple ML-based mood prediction model using scikit-learn.
- **storytelling_module.py** → Collaborative writing and illustrating workflow.


## Running the Application

1. Open a terminal in this folder.

2. Install required dependencies:
pip install streamlit bcrypt PyJWT pandas numpy matplotlib scikit-learn

3. Run the Streamlit app:

streamlit run streamlit_hub_app.py

4. The app will open automatically in your browser at http://localhost:8501.


## Features

- Authentication: Register/login with hashed passwords and JWT tokens.
- Logging: Tracks actions (logins, uploads, mood predictions, story entries).
- Dashboard: Displays simulated mental health data trends with interactive charts.
- Mood Prediction: Predicts a user's mood category based on demo inputs.
- Collaborative Storytelling: Writers and illustrators co-create stories in a shared workflow.

## Notes

- This hub is designed for demonstration and learning purposes.
- Session state is used instead of a persistent database.
- The modular structure makes it easy to extend or replace individual components.
- The Mood Predictor and Dashboard modules are based on code and contributions from collaborator **Bhanu Pratap Singh Mehar**, integrated here into the hub application.
