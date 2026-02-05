def generate_cover_letter(client, profile, job_description):
    """
    Generates a personalized, ethical cover letter.
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an ethical AI cover letter assistant. "
                    "Write concise, honest, and job-specific cover letters."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Candidate Profile:\n{profile}\n\n"
                    f"Job Description:\n{job_description}\n\n"
                    "Write a professional cover letter."
                )
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content

