import os
import streamlit as st
os.environ["GOOGLE_API_KEY"] = "AIzaSyCvWsMquBzxCDbsfu8qB7jOik9WG04xksw"

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
st.set_page_config(page_title="CHINTU BOLAAA !!!", page_icon="🤖", layout="centered")

# App Title
st.markdown("<h1 style='text-align: center; color: #00b8e6;'>🤖 HEYDOC BOT</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Your smart AI assistant to summarize anything!</h4>", unsafe_allow_html=True)

# Ask for user's name
user_name = st.text_input("👋 Hi there! What's your name?", placeholder="Enter your name")

if user_name:
    st.success(f"Hello, {user_name}! 👨‍⚕️ Ready to summarize your prompt?")
    user_input = st.text_input("💬 Type your prompt here:")
    
    if st.button("🧠 Summarize"):
        if user_input:
            with st.spinner("Thinking... 🤔"):
                result = model.invoke(user_input)
            st.markdown("### ✨ Summary:")
            st.success(result.content)
        else:
            st.warning("Please enter a prompt to summarize.")
else:
    st.info("Please enter your name to begin 😊")
# Footer with your credit
st.markdown("""
<hr style='margin-top: 50px;'>
<div style='text-align: center; color: #888;'>
    Made with ❤️ by <strong>Aman Srivastava</strong><br>
    <small>Powered by Gemini 1.5 Pro & LangChain</small>
</div>
""", unsafe_allow_html=True)



