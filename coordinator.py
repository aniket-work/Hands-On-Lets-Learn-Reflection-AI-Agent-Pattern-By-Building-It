def completions_create(client, messages: list, model: str) -> str:

    response = client.chat.completions.create(messages=messages, model=model)
    return str(response.choices[0].message.content)


def build_prompt_structure(prompt: str, role: str, tag: str = "") -> dict:

    if tag:
        prompt = f"<{tag}>{prompt}</{tag}>"
    return {"role": role, "content": prompt}


def update_chat_history(history: list, msg: str, role: str):

    history.append(build_prompt_structure(prompt=msg, role=role))


class Curator(list):
    def __init__(self, messages: list | None = None, total_length: int = -1):

        if messages is None:
            messages = []

        super().__init__(messages)
        self.total_length = total_length

    def append(self, msg: str):

        if len(self) == self.total_length:
            self.pop(0)
        super().append(msg)


class Padder(Curator):
    def __init__(self, messages: list | None = None, total_length: int = -1):

        super().__init__(messages, total_length)

    def append(self, msg: str):

        if len(self) == self.total_length:
            self.pop(1)
        super().append(msg)