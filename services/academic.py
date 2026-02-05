def improve_academic_writing(client, text, citation_style):
    """
    Improves academic writing ethically with citation awareness.
    """
    # Guard against empty text
    if not text.strip():
        return "No text provided."

    response = client.chat.completions.create(
        model="llama2-7b-chat",  # safe model
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an ethical academic writing assistant. "
                    "Improve clarity, structure, and grammar. "
                    "Do NOT generate false citations. "
                    f"Use {citation_style} citation style if needed."
                )
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0.4
    )

    # Return the improved text safely
    return response.choices[0].message.content

