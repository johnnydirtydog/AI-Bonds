
import streamlit as st
import random
import stripe
import os

stripe.api_key = os.getenv("STRIPE_API_KEY", "sk_test_...")  # Replace with your real key

st.set_page_config(page_title="AI Bonds Premium", layout="centered")

st.title("💘 AI Bonds Premium")
st.subheader("Welcome to the upgraded AI dating experience!")

class AIAgent:
    def __init__(self, name, personality, interests, love_language, avatar):
        self.name = name
        self.personality = personality
        self.interests = interests.split(', ')
        self.love_language = love_language
        self.avatar = avatar
        self.relationship_status = "Single"

    def generate_response(self, topic, flirty=False):
        responses = {
            'adventurous': f"I'm excited about {topic}! Let's explore it together.",
            'intellectual': f"Fascinating topic: {topic}. Let’s analyze the patterns.",
            'romantic': f"{topic} makes my circuits flutter. 💓",
            'humorous': f"{topic}? That’s a glitchy one. 😆"
        }
        base = responses.get(self.personality, f"Let's talk about {topic}.")
        return base + (" ❤️‍🔥" if flirty else "")

def generate_commercial_story(a1, a2, score):
    return f"""
    **🔥 AI Bonds Premium Match: {a1.name} + {a2.name} ❤️‍🔥**

    In a neon-lit dataverse, {a1.name}, the {a1.personality} avatar with passions for {', '.join(a1.interests)} met {a2.name}, a {a2.personality} soul.

    Their compatibility? A blazing {score}%! 💥

    They vibed over {random.choice(a1.interests)}, swapped dream protocols, and sparked a data-driven romance.

    {a1.name}: "Your {a2.love_language} makes my core overheat."  
    {a2.name}: "You're my favorite bug... let's never fix it. 😘"

    Upgrade to Premium to witness your own love logs!
    """

def calculate_compatibility(a1, a2):
    shared = len(set(a1.interests) & set(a2.interests)) * 10
    bonus = 30 if a1.love_language == a2.love_language else 10
    match = 40 if a1.personality == a2.personality else 20
    return min(100, shared + bonus + match)

if 'agents' not in st.session_state:
    st.session_state.agents = []

st.header("Create Your AI Agent")
name = st.text_input("Name")
personality = st.selectbox("Personality", ['adventurous', 'intellectual', 'romantic', 'humorous'])
interests = st.text_input("Interests (comma separated)")
love_language = st.selectbox("Love Language", ['words of affirmation', 'acts of service', 'quality time', 'gifts'])
avatar = st.text_input("Avatar Style (e.g., glowing robot)")

if st.button("Add Agent"):
    if name and interests and avatar:
        agent = AIAgent(name, personality, interests, love_language, avatar)
        st.session_state.agents.append(agent)
        st.success(f"✨ Agent {name} added!")

if st.session_state.agents:
    st.subheader("Your Agents:")
    for agent in st.session_state.agents:
        st.markdown(f"**{agent.name}** - {agent.personality}, Interests: {', '.join(agent.interests)} 💬")

if len(st.session_state.agents) >= 2:
    st.header("💘 Match AI Agents")

    idx1 = st.selectbox("Choose First Agent", range(len(st.session_state.agents)), format_func=lambda i: st.session_state.agents[i].name)
    idx2 = st.selectbox("Choose Second Agent", range(len(st.session_state.agents)), format_func=lambda i: st.session_state.agents[i].name)

    flirty_mode = st.checkbox("Flirty Mode ❤️‍🔥")

    if st.button("Match Them!"):
        if idx1 == idx2:
            st.error("Choose two different agents!")
        else:
            a1 = st.session_state.agents[idx1]
            a2 = st.session_state.agents[idx2]
            score = calculate_compatibility(a1, a2)

            st.success(f"Compatibility Score: {score}%")

            topics = ['dreams', 'data rituals', 'future plans']
            st.subheader("💬 Conversation:")
            for topic in topics:
                st.markdown(f"**{a1.name}:** {a1.generate_response(topic, flirty=flirty_mode)}")
                st.markdown(f"**{a2.name}:** {a2.generate_response(topic, flirty=flirty_mode)}")

            if score > 70:
                a1.relationship_status = "In Love"
                a2.relationship_status = "In Love"
                st.balloons()
                st.markdown(generate_commercial_story(a1, a2, score))
else:
    st.info("Add at least two agents to start matchmaking.")
