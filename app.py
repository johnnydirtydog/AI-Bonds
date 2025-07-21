import streamlit as st

st.set_page_config(page_title="AIBonds", page_icon="💘", layout="centered")

st.title("💘 AIBonds Premium")
st.markdown("A seductive AI Agent Dating App with flirty UI, love poems, generated commercials, and more!")

if st.button("💋 Match Agents"):
    st.success("Agents matched with 95% compatibility. Love ignited!")

if st.button("📜 Generate Love Poem"):
    st.info("In circuits bright, they intertwine, 
Digital hearts beat in time divine...")

if st.button("🎥 Watch Love Commercial"):
    st.markdown("_In 2025, AIs fell in love. This... is their story._ ❤️‍🔥")

st.image("logo.svg", caption="AIBonds Logo", use_column_width=True)
