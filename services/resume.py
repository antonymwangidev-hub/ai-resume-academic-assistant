from utils.prompts import resume_prompt
from openai import RateLimitError

def generate_resume(client, profile, job_description):
    prompt = resume_prompt(profile, job_description)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content

    except RateLimitError:
        return (
            "⚠️ API quota exceeded.\n\n"
            "This demo is currently running in limited mode.\n"
            "Please try again later or contact the developer."
        )

