from utils.prompts import academic_prompt
from openai import RateLimitError

def improve_academic_text(client, text, citation_style):
    prompt = academic_prompt(text, citation_style)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content

    except RateLimitError:
        return (
            "⚠️ API quota exceeded.\n\n"
            "Academic writing assistance is temporarily unavailable."
        )

