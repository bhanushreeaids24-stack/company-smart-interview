
import streamlit as st

st.set_page_config(
    page_title="Company-Smart Interview Coach",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Company-Smart Mock Interview Coach")

st.subheader("Your Personal AI Interview Preparation Assistant")

st.write(
    "Prepare for company-specific interviews "
    "with AI-powered questions, evaluation and coaching."
)

st.divider()

st.header("Start Your Interview")

student_name = st.text_input("Enter your name")

company = st.selectbox(
    "Select your target company",
    ["Infosys", "TCS", "Wipro", "Accenture", "Google"]
)

role = st.selectbox(
    "Select your job role",
    ["Python Developer", "Java Developer",
     "Software Engineer", "Data Analyst"]
)

if st.button("Start Mock Interview"):
    if student_name:
        st.success("Welcome " + student_name + "!")
        st.write("Company:", company)
        st.write("Role:", role)
        st.info("Your AI interview preparation journey starts here!")
    else:
        st.warning("Please enter your name.")
