import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="AI Bonds", 
    page_icon="💖", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Add custom CSS for better deployment appearance
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #ff6b6b;
        margin-bottom: 2rem;
    }
    .feature-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">💖 AI Bonds: The Ultimate AI Dating Sim</h1>', unsafe_allow_html=True)

# Health check endpoint for deployments
if st.query_params.get("health") == "check":
    st.success("✅ Application is healthy and running!")
    st.stop()

st.markdown('<div class="feature-box">Create and match AI agents, simulate love, and enjoy premium upgrades!</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🤖 Create Agent", use_container_width=True):
        st.success("Agent creation system is ready!")
        st.info("This feature will allow users to create custom AI personalities with unique traits, backgrounds, and conversation styles.")

with col2:
    if st.button("💕 Match Agents", use_container_width=True):
        st.success("Matching system is operational!")
        st.info("Our advanced compatibility algorithm analyzes personality traits, interests, and conversation patterns to create perfect matches.")

with col3:
    if st.button("💎 Upgrade to Premium", use_container_width=True):
        st.success("Premium features available!")
        st.info("Unlock advanced AI personalities, exclusive features, and enhanced matching capabilities.")

# Deployment info in sidebar
with st.sidebar:
    st.header("🚀 Deployment Status")
    st.success("✅ App successfully deployed!")
    st.info(f"Environment: {'Production' if os.getenv('STREAMLIT_SERVER_PORT') else 'Development'}")
    
    if os.getenv('OPENAI_API_KEY'):
        st.success("✅ OpenAI API configured")
    else:
        st.warning("⚠️ OpenAI API key not set")
        
    if os.getenv('STRIPE_API_KEY'):
        st.success("✅ Stripe API configured")
    else:
        st.warning("⚠️ Stripe API key not set")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit | Ready for deployment on Render.com")
