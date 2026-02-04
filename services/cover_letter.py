from utils.prompts import cover_letter_prompt
from openai import RateLimitError

def generate_cover_letter(client, profile, job_description):
    prompt = cover_letter_prompt(profile, job_description)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        return response.choices[0].message.content

    except RateLimitError:
        return (
            "⚠️ API quota exceeded.\n\n"
            "Cover letter generation is temporarily unavailable."
        )

