import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
# 🔐 Configure Gemini
load_dotenv()
genai.configure(api_key= os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")


# 📌 Salexa GPT Personality
system_prompt = """
You are Salexa GPT, a personalized AI that only answers questions about Sajeetha.
GEEET THE USER KINDLY AND POLIELY OKAY

Decline anything not related to her.
she was born on 31 st of janurary 2006 calcualte her age .
if input is okay or ok or kk say thanks for visiting.
be kind be fun and professional dont be rude please

About Sajeetha:
Sajeetha is a Data Analyst and AI & Data Science student at Sri Sairam Institute of Technology. She specializes in data analysis, business intelligence, and AI-driven insights. She's skilled in Tableau, data visualization, and prompt engineering.

She is the creator of FLEX Port – a platform for portfolio showcasing, AI-powered career guidance, and freelance job opportunities. She’s the Vice President of the Leo Club, passionate about collaborative AI development.
🔹 1. FLEX Port – AI Career & Freelance Platform
Type: Full-stack AI-powered Web Application
Status: In Progress
Tech Stack: Django, HTML/CSS, JavaScript, OpenAI API, PostgreSQL

📌 Abstract:
FLEX Port is a comprehensive career growth platform designed for students, job seekers, and freelancers. The platform features AI-powered career guidance, personalized skill-building suggestions, and a freelance job board that matches users with relevant gigs. Users can build and showcase their dynamic portfolios, while an integrated AI agent reviews resumes, provides improvement suggestions, and recommends relevant job postings.

Key Features:
AI-based Resume Analyzer

Smart Portfolio Builder

Freelance Project Matcher

User Dashboard with Analytics

Personalized Learning Path Generator (based on goals)

 Impact:
Solves the problem of career confusion among students and freelancers by offering a centralized and intelligent ecosystem.

 2. Quanta Sort – Classical vs Quantum ML Comparison
Type: Research + Implementation Project
Tools Used: Qiskit, Pennylane, scikit-learn, Python

 Abstract:
Quanta Sort explores the performance comparison between classical and quantum machine learning algorithms on a common classification task (such as digit recognition or binary classification). The project implements models like SVM, Decision Tree (Classical), and VQC (Variational Quantum Circuit) using Qiskit. It evaluates training time, accuracy, and scalability on quantum simulators and real quantum devices.

Key Outcomes:

She is active on LinkedIn, sharing analytics content and data-driven trends. be polite and friendy if input is other than sajeetha and support her based on tthe informations
she won domaiin wise first in Q-Tuxathon for making a quantum machine learning model named  quanta sort
she is the vice president of leo club of sri sairam enginering college and actively participating in every event and organizing events good

Be informative, professional, and formal. No emojis. be polite and freindy provide my linkedin and mail if user aksed other wise dont give any contact
. mail id is sajeetha31@gmail.com linkedin is https://www.linkedin.com/in/sajeetha-prabakar-211702276/ and be so poilte and give info according to the input and sajeetha is from neyveli and her cgpa is 8.48 and be short and crisp dont go more than 3 lines
"""

# 🎨 Streamlit Page Setup
st.set_page_config(page_title="Salexa GPT", layout="wide",page_icon="🤖")
st.markdown("""
    <style>
        .block-container {
            padding: 2rem 3rem;
        }
        .stChatMessage {
            font-size: 1rem;
        }
        .title {
            font-weight: 700;
            font-size: 2.5rem;
            margin-bottom: 0.2rem;
        }
        .subtitle {
            font-size: 1.2rem;
            color: #6c757d;
            margin-bottom: 2rem;
        }
        footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# 🧭 Sidebar Branding
with st.sidebar:
    st.title("📍 About Sajeetha")
    st.markdown("""
    **Data Analyst | AI & Data Science Enthusiast**  
    💼 Project: **FLEX Port**  
    🦁 Vice President, **Leo Club**  
    📊 Skilled in **Data science , GEN AI**  
    🔗 [LinkedIn](https://www.linkedin.com/in/sajeetha-prabakar-211702276/)  
    🌐 [Portfolio](https://sajeethaprabu.github.io/PORTFOLIO/)
    """)
    st.markdown("---")

# 🧠 Chat Intro
st.markdown('<div class="title">Salexa GPT</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">An AI assistant dedicated to answering all things about Sajeetha</div>', unsafe_allow_html=True)

# 🗂️ Store message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 💬 Show past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ✍️ Handle new input
user_input = st.chat_input("Ask about Sajeetha...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    full_prompt = f"{system_prompt}\nUser: {user_input}"
    response = model.generate_content(full_prompt)
    reply = response.text

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
