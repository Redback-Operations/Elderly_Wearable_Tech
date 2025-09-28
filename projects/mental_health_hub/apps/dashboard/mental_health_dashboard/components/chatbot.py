import streamlit as st
import openai
from utils.sanitizer import sanitize_input

def chatbot_box(mood_score):
    openai.api_key = st.secrets.get("OPENAI_API_KEY")
    st.sidebar.markdown("## 🤖 Chat with Wellness Assistant")
    st.sidebar.write("🔐 Key loaded:", "✅" if openai.api_key else "❌ Not found")
    user_query = st.sidebar.text_input("Ask anything (e.g., Tips for better sleep)")

    if user_query:
        clean_input = sanitize_input(user_query)
        prompt = f"""
        You are a friendly wellness assistant for elderly users.
        Mood score: {mood_score}/100.
        User asked: \"{clean_input}\".
        If mood < 65, be gentle. Else share a wellness tip. Max 100 words.
        """
        try:
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.7
            )
            reply = res.choices[0].message["content"]
        except:
            reply = "⚠️ Chatbot error: Check your OpenAI key or connection."

        st.sidebar.markdown("**Assistant Response:**")
        st.sidebar.success(reply)
        if mood_score < 65:
            st.sidebar.markdown("\n💡 *You seem a bit down today. Try calling a loved one or taking a short walk.*")


