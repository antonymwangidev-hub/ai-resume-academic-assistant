def improve_academic_writing(client, text, citation_style):
    """
    Improves academic writing ethically with citation awareness.
    """

    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
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
                "content": (
                    f"Academic Text:\n{text}\n\n"
                    "Improve this text while preserving the original meaning."
                )
            }
        ],
        temperature=0.4
    )

    return response.choices[0].message.content

