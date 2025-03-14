from pathlib import Path
from jinja2 import Environment, FileSystemLoader

def build_prompt_structure(prompt: str, role: str) -> dict:
    """Structure prompts for LLM consumption"""
    return {"role": role, "content": prompt}

def update_chat_history(history: list, msg: str, role: str):
    """Update chat history with new message"""
    history.append(build_prompt_structure(msg, role))

def load_template(template_name: str) -> str:
    """Load Jinja2 templates from config"""
    env = Environment(
        loader=FileSystemLoader(Path(__file__).parent.parent.parent / "config/prompts")
    )
    return env.get_template(template_name).render()

class Padder(list):
    """Maintain chat history with fixed first message"""
    def __init__(self, messages: list, total_length: int):
        super().__init__(messages)
        self.total_length = total_length

    def append(self, msg: str):
        if len(self) >= self.total_length:
            self.pop(1)
        super().append(msg)