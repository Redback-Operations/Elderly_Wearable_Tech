import streamlit as st

def support_section():
    st.markdown("### 📞 Get Support")
    st.markdown("""
    - [Lifeline – 13 11 14](https://www.lifeline.org.au)
    - [Beyond Blue](https://www.beyondblue.org.au)
    - [Carer Gateway](https://www.carergateway.gov.au/)
    """)

import streamlit.components.v1 as components

def mindfulness_gif():
    st.markdown("### 🌬️ Guided Breathing Exercise")
    st.markdown("Follow the circle below. Inhale as it expands, exhale as it contracts.")

    components.html("""
    <style>
        .circle {
            width: 150px;
            height: 150px;
            margin: 40px auto;
            border-radius: 50%;
            background-color: #a5d6a7;
            animation: breathe 8s ease-in-out infinite;
        }

        @keyframes breathe {
            0% { transform: scale(1); opacity: 0.8; }
            50% { transform: scale(1.5); opacity: 1; }
            100% { transform: scale(1); opacity: 0.8; }
        }

        .breathe-instruction {
            text-align: center;
            font-size: 18px;
            font-weight: 500;
            margin-top: -20px;
            color: #333;
        }
    </style>

    <div class="circle"></div>
    <div class="breathe-instruction">Inhale... Exhale... Relax</div>
    """, height=250)

    with st.expander("🔊 Optional: Play calming audio"):
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
