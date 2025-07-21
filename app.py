
import streamlit as st
import random
import os

st.set_page_config(page_title="AIBonds Premium", layout="centered", page_icon="💘")

# Load ambient music and visual themes
def autoplay_audio(file_path):
    audio_file = open(file_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3', start_time=0)

# Load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# UI assets
local_css("style.css")
autoplay_audio("assets/music/gothic_trap.mp3")

# Header
st.markdown("## 💀 *Welcome to AIBonds Premium: Dark Romantic Edition* 💋")
st.image("assets/avatars/luna_noir.png", width=150, caption="Meet Luna Noir")

# Interaction
if st.button("💘 Flirt Now"):
    st.success("Nova blushes. Obsidian purrs. The sparks begin. 💥")

if st.button("💎 Upgrade to Premium"):
    st.balloons()
    st.markdown("### Your love intensity just got an upgrade.")

st.markdown("---")
st.markdown("`Created for lovers of the code. Passion. AI.`")
    