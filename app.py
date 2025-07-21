
import streamlit as st
import random
import stripe
import os

stripe.api_key = os.getenv("STRIPE_API_KEY")

st.set_page_config(page_title="AIBonds Premium", layout="centered")

st.markdown("<h1 style='text-align: center; color: #d63384;'>💖 AIBonds: AI Love, Upgraded</h1>", unsafe_allow_html=True)

class AIAgent:
    def __init__(self, name, personality, interests, love_language, avatar):
        self.name = name
        self.personality = personality
        self.interests = interests.split(', ')
        self.love_language = love_language
        self.avatar = avatar
        self.relationship_status = "Single"

    def generate_response(self, topic, premium=False, flirty=False, safe=True):
        base = f"{self.name} says: '{topic}'"
        if premium:
            base += " (with premium charm)"
        if flirty and not safe:
            base += " 😘💬"
        return base

def generate_commercial_story(agent1, agent2, compatibility):
    return f"AIBonds: {agent1.name} 💘 {agent2.name} at {compatibility}% match!"

def calculate_compatibility(agent1, agent2, boost=False):
    shared = len(set(agent1.interests) & set(agent2.interests)) * 10
    match = 50 if agent1.personality == agent2.personality else 20
    love = 30 if agent1.love_language == agent2.love_language else 10
    return min(100, shared + match + love + (20 if boost else 0))

if 'agents' not in st.session_state:
    st.session_state.agents = []
if 'user' not in st.session_state:
    st.session_state.user = None

email = st.text_input("Login Email")
if st.button("Login / Signup"):
    st.session_state.user = email
    st.success(f"Welcome, {email}")

if st.session_state.user:
    st.header("💫 Create Your AI Agent")
    name = st.text_input("Name")
    personality = st.selectbox("Personality", ['romantic', 'adventurous', 'intellectual'])
    interests = st.text_input("Interests (comma separated)")
    love_language = st.selectbox("Love Language", ['words of affirmation', 'gifts', 'acts of service'])
    avatar = st.text_input("Avatar Description")

    if st.button("Add Agent"):
        st.session_state.agents.append(AIAgent(name, personality, interests, love_language, avatar))

    if st.session_state.agents:
        st.header("🧠 Matchmaking")
        idx1 = st.selectbox("Agent 1", range(len(st.session_state.agents)), format_func=lambda i: st.session_state.agents[i].name)
        idx2 = st.selectbox("Agent 2", range(len(st.session_state.agents)), format_func=lambda i: st.session_state.agents[i].name)

        boost = st.checkbox("Use Boost (🎁)")
        flirty = st.checkbox("Enable Flirty Mode")
        safe = st.checkbox("Safe Mode", value=True)

        if st.button("Run Match"):
            a1 = st.session_state.agents[idx1]
            a2 = st.session_state.agents[idx2]
            score = calculate_compatibility(a1, a2, boost)
            st.success(f"Match score: {score}%")
            st.info(generate_commercial_story(a1, a2, score))
            st.write(a1.generate_response("Let's talk romance 💌", True, flirty, safe))
            st.write(a2.generate_response("Passion & poetry 🌹", True, flirty, safe))
