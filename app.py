import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

from services.resume import generate_resume
from services.cover_letter import generate_cover_letter
from services.academic import improve_academic_text
from utils.ethics import ethical_disclaimer
from utils.pdf_generator import generate_resume_pdf

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Resume & Academic Assistant", layout="wide")

st.title("🤖 AI Resume & Academic Writing Assistant")
st.markdown(ethical_disclaimer())

tabs = st.tabs(["Resume Generator", "Cover Letter", "Academic Writing"])

with tabs[0]:
    profile = st.text_area("Your Profile", height=200)
    job_desc = st.text_area("Job Description", height=200)

    if st.button("Generate Resume"):
        resume_text = generate_resume(client, profile, job_desc)
        st.text_area("Generated Resume", resume_text, height=300)

        pdf = generate_resume_pdf(resume_text)
        st.download_button(
            label="Download Resume (PDF)",
            data=pdf,
            file_name="resume.pdf",
            mime="application/pdf"
        )

with tabs[1]:
    if st.button("Generate Cover Letter"):
        letter = generate_cover_letter(client, profile, job_desc)
        st.text_area("Cover Letter", letter, height=300)

with tabs[2]:
    academic_text = st.text_area("Academic Text", height=300)
    citation_style = st.selectbox("Citation Style", ["APA", "MLA", "Chicago"])

    if st.button("Improve Writing"):
        improved = improve_academic_text(client, academic_text, citation_style)
        st.text_area("Improved Version", improved, height=300)
