def resume_prompt(profile, job_description):
    return f"""
You are an ethical AI resume assistant.

Generate a professional ATS-friendly resume.

PROFILE:
{profile}

JOB DESCRIPTION:
{job_description}

RULES:
- Do not invent experience
- Keep content truthful
- Use bullet points
"""

def cover_letter_prompt(profile, job_description):
    return f"""
Write a professional cover letter using only the information provided.

PROFILE:
{profile}

JOB DESCRIPTION:
{job_description}

RULES:
- No fabricated achievements
- Professional tone
"""

def academic_prompt(text, citation_style):
    return f"""
Improve clarity and structure of the academic text below.

TEXT:
{text}

RULES:
- Preserve meaning
- Avoid plagiarism
- Suggest citations
- Citation style: {citation_style}
"""
