import streamlit as st
from openai import OpenAI
import io

API_KEY="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"

client=OpenAI(api_key=API_KEY,base_url="https://api.groq.com/openai/v1")

st.set_page_config(page_title="📊 Math Genie", layout="centered")
st.title("📊 Math Genie")

# 2. Example Problem Customization
with st.expander("🧠 My Example Problems"):
    st.markdown("""
    **Probability:** Tossing coins, rolling dice
    - Example: "What's the probability of getting heads twice in 3 coin tosses?"
    
    **Algebra:** Word problems and equations
    - Example: "A number increased by 5 is 12. What’s the number?"
    """)

level =     .selectbox("Choose your level", ["Beginner", "Regular", "Challenging"], index=1)

system_prompt = """You are a Math Wizard built by Aanya – always precise, patient, and full of clarity.
For every math problem:
1. Show detailed steps
2. Explain the method
3. Highlight the final answer"""
