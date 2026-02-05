import os
import streamlit as st
from groq import Groq

from services.resume import generate_resume
from services.cover_letter import generate_cover_letter
from services.academic import improve_academic_writing
from utils.pdf_generator import generate_pdf


# ----------------------------
# App Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Resume & Academic Writing Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI-Powered Resume & Academic Writing Assistant")
st.caption("Ethical AI • Fast Inference • ATS-Friendly • Academic Integrity")


# ----------------------------
# Initialize Groq Client
# ----------------------------
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# ----------------------------
# Sidebar Navigation
# ----------------------------
tool = st.sidebar.selectbox(
    "Choose a tool",
    [
        "Resume Generator",
        "Cover Letter Generator",
        "Academic Writing Assistant"
    ]
)


# ----------------------------
# Resume Generator
# ----------------------------
if tool == "Resume Generator":
    st.header("🧾 Resume Generator")

    profile = st.text_area(
        "Candidate Profile",
        placeholder="Paste skills, experience, education, achievements...",
        height=200
    )

    job_desc = st.text_area(
        "Job Description",
        placeholder="Paste the target job description...",
        height=200
    )

    if st.button("Generate Resume"):
        if profile and job_desc:
            with st.spinner("Generating resume..."):
                resume_text = generate_resume(client, profile, job_desc)

            st.subheader("Generated Resume")
            st.text_area("", resume_text, height=400)

            pdf_bytes = generate_pdf(resume_text, "resume.pdf")
            st.download_button(
                "📥 Download Resume (PDF)",
                data=pdf_bytes,
                file_name="resume.pdf",
                mime="application/pdf"
            )
        else:
            st.warning("Please fill in both fields.")


# ----------------------------
# Cover Letter Generator
# ----------------------------
elif tool == "Cover Letter Generator":
    st.header("✉️ Cover Letter Generator")

    profile = st.text_area(
        "Candidate Profile",
        placeholder="Paste your professional background...",
        height=200
    )

    job_desc = st.text_area(
        "Job Description",
        placeholder="Paste the job description...",
        height=200
    )

    if st.button("Generate Cover Letter"):
        if profile and job_desc:
            with st.spinner("Generating cover letter..."):
                cover_letter = generate_cover_letter(client, profile, job_desc)

            st.subheader("Generated Cover Letter")
            st.text_area("", cover_letter, height=400)

            pdf_bytes = generate_pdf(cover_letter, "cover_letter.pdf")
            st.download_button(
                "📥 Download Cover Letter (PDF)",
                data=pdf_bytes,
                file_name="cover_letter.pdf",
                mime="application/pdf"
            )
        else:
            st.warning("Please fill in both fields.")


# ----------------------------
# Academic Writing Assistant
# ----------------------------
elif tool == "Academic Writing Assistant":
    st.header("🎓 Academic Writing Assistant (Ethical)")

    academic_text = st.text_area(
        "Academic Text",
        placeholder="Paste your essay, paper, or report...",
        height=300
    )

    citation_style = st.selectbox(
        "Citation Style",
        ["APA", "MLA", "Chicago", "Harvard"]
    )

    if st.button("Improve Writing"):
        if academic_text:
            with st.spinner("Improving academic writing..."):
                improved_text = improve_academic_writing(
                    client,
                    academic_text,
                    citation_style
                )

            st.subheader("Improved Academic Text")
            st.text_area("", improved_text, height=400)

            pdf_bytes = generate_pdf(improved_text, "academic_text.pdf")
            st.download_button(
                "📥 Download Improved Text (PDF)",
                data=pdf_bytes,
                file_name="academic_text.pdf",
                mime="application/pdf"
            )
        else:
            st.warning("Please paste academic text.")

