from groq import Groq
from colorama import Fore, Style
from ..utils.llm import completions_create
from ..utils.loggers import observer


class DeveloperAgent:
    """AI developer agent for code generation"""

    def __init__(self, model: str = "llama3-70b-8192"):
        self.client = Groq()
        self.model = model

    def generate_code(self, history: list) -> str:
        response = completions_create(self.client, history, self.model)
        return f"\n{Fore.BLUE}💻 DEVELOPER SUBMISSION{Style.RESET_ALL}\n{response}"


class TesterAgent:
    """AI tester agent for code analysis"""

    def __init__(self, model: str = "mixtral-8x7b-32768"):
        self.client = Groq()
        self.model = model

    def analyze_code(self, history: list) -> str:
        response = completions_create(self.client, history, self.model)
        return f"\n{Fore.GREEN}📋 TESTER ANALYSIS{Style.RESET_ALL}\n{response}"