import streamlit as st

mood = st.selectbox("Agent Mood", ["neutral", "flirty"])
if mood == "flirty":
    st.image("avatars/flirty_agent1.gif", caption="Flirty Agent")
else:
    st.write("Mood is neutral.")
