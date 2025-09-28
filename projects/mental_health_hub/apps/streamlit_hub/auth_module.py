import streamlit as st
import bcrypt # Import bcrypt and jwt functionality
import jwt
import datetime
from logging_module import log_event  # Import log_event function

# Secret key for signing JWTs
SECRET_KEY = "super-secret-key"

# In-memory "database" for demo
if "users_db" not in st.session_state:
    st.session_state.users_db = {}

# Session state for authentication
if "token" not in st.session_state:
    st.session_state.token = None
if "user" not in st.session_state:
    st.session_state.user = None


# Hash password, bcrypt, token generation, verification functionality
def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed)

def generate_token(username: str) -> str:
    payload = {
        "user": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


# Streamlit User-Interface
def run_auth():
    st.title("🔑 User Authentication (JWT)")

    choice = st.radio("Choose Action:", ["Login", "Register", "Logout"])

    # Register functionality
    if choice == "Register":
        st.subheader("Create a new account")
        username = st.text_input("Username (register)")
        password = st.text_input("Password (register)", type="password")

        if st.button("Register"):
            if username in st.session_state.users_db:
                st.error("User already exists.")
                log_event(f"Failed registration attempt (user exists): {username}", 'ERROR')  # Log failed registration
            else:
                st.session_state.users_db[username] = hash_password(password)
                st.success(f"User {username} registered successfully!")
                log_event(f"User successfully registered: {username}", 'INFO')  # Log the successful registration event

    # Login Functionality
    elif choice == "Login":
        st.subheader("Login")
        username = st.text_input("Username (login)")
        password = st.text_input("Password (login)", type="password")

        if st.button("Login"):
            if username not in st.session_state.users_db:
                st.error("Invalid credentials.")
                log_event(f"Failed login attempt (user does not exist): {username}", 'ERROR')  # Log failed login
            else:
                stored_pw = st.session_state.users_db[username]
                if verify_password(password, stored_pw):
                    token = generate_token(username)
                    st.session_state.token = token
                    st.session_state.user = username
                    st.success(f"Welcome, {username}!")
                    log_event(f"User successfuly logged in: {username}", 'INFO')  # Log successful login
                else:
                    st.error("Invalid credentials.")
                    log_event(f"Failed login attempt (incorrect password): {username}", 'ERROR')  # Log failed login

    # Logout functionality
    elif choice == "Logout":
        if st.session_state.token:
            log_event(f"User logged out: {st.session_state.user}", 'INFO')  # Log the logout event
            st.session_state.token = None
            st.session_state.user = None
            st.success("You have successfully been logged out.")
        else:
            st.info("You are not logged in.")

    # Protected Area
    if st.session_state.token:
        payload = verify_token(st.session_state.token)
        if payload:
            st.info(f"🔒 Protected: Hello {payload['user']}!")
        else:
            st.error("Your session expired. Please login again.")
            log_event(f"Session expired for: {st.session_state.user}", 'ERROR')  # Log session expiry event
            st.session_state.token = None
            st.session_state.user = None
