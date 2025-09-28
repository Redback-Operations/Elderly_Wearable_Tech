# components/game_mind_match.py

import streamlit as st
import random
import time

def play_mind_match():
    st.subheader("🧠 Mind Match — Memory Game")
    st.markdown("Match all the calming pairs! Refresh to reset.")

    emojis = ["🌞", "🌙", "🌸", "🍀", "☁️", "🔥", "💧", "🌈"]
    pairs = emojis * 2
    random.shuffle(pairs)

    if "matched" not in st.session_state:
        st.session_state.matched = [False] * 16
        st.session_state.selected = []
        st.session_state.pairs = pairs
        st.session_state.moves = 0

    cols = st.columns(4)
    for i in range(16):
        with cols[i % 4]:
            if st.session_state.matched[i]:
                st.button(st.session_state.pairs[i], key=f"btn_{i}", disabled=True)
            elif i in st.session_state.selected:
                st.button(st.session_state.pairs[i], key=f"btn_{i}", disabled=True)
            else:
                if st.button("❓", key=f"btn_{i}"):
                    st.session_state.selected.append(i)

    if len(st.session_state.selected) == 2:
        i, j = st.session_state.selected
        if st.session_state.pairs[i] == st.session_state.pairs[j]:
            st.session_state.matched[i] = True
            st.session_state.matched[j] = True
        time.sleep(0.5)
        st.session_state.selected = []
        st.session_state.moves += 1

    if all(st.session_state.matched):
        st.success(f"🎉 Great job! You matched all pairs in {st.session_state.moves} moves.")
