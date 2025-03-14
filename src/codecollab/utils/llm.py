def completions_create(client, messages: list, model: str) -> str:
    response = client.chat.completions.create(
        messages=messages,
        model=model
    )
    return str(response.choices[0].message.content)