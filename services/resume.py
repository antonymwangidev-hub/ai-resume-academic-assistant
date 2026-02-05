def generate_resume(client, profile, job_description):
    """
    Generates an ATS-friendly resume using Groq LLMs.
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an ethical AI resume writer. "
                    "Generate professional, ATS-friendly resumes. "
                    "Do not fabricate experience or credentials."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Candidate Profile:\n{profile}\n\n"
                    f"Target Job Description:\n{job_description}\n\n"
                    "Generate a tailored resume."
                )
            }
        ],
        temperature=0.6
    )

    return response.choices[0].message.content

