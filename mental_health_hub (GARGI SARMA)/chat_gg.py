import streamlit as st
import time

# Initialize chat history in session state
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

def run_chat():
    st.title("Streamlit Group Chat (No Server)")

    nickname = st.text_input("Choose a nickname", key="nickname")
    if not nickname:
        st.info("Enter a nickname to join the chat.")
        st.stop()

    # Display chat history
    st.subheader("Chat Room")
    chat_box = st.empty()
    for msg in st.session_state.chat_messages:
        chat_box.write(msg)

    # Message input
    msg = st.text_input("Type your message", key="msg")
    if st.button("Send"):
        if msg:
            message = f"{nickname}: {msg}"
            st.session_state.chat_messages.append(message)
            st.experimental_rerun()

    # Optionally, auto-refresh every few seconds for a "live" feel
    st.button("Refresh Chat")