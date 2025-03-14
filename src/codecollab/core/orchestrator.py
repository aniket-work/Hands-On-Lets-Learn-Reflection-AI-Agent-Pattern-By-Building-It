from colorama import Fore
from ..utils.helpers import build_prompt_structure, update_chat_history, Padder
from ..utils.loggers import observer
from config import constants


class DevTestOrchestrator:
    """Orchestration engine for developer-tester collaboration"""

    def __init__(self, developer, tester):
        self.developer = developer
        self.tester = tester

    def _print_banner(self, text: str):
        border = constants.EMOJIS["border"] * 30
        print(f"\n{Fore.MAGENTA}{border}")
        print(f"{text.center(30)}")
        print(f"{border}{Style.RESET_ALL}\n")

    def run_cycle(self, user_request: str, max_cycles: int = 4):
        dev_history = Padder([
            build_prompt_structure(constants.PROMPTS["developer"], "system"),
            build_prompt_structure(user_request, "user")
        ], total_length=5)

        test_history = Padder([
            build_prompt_structure(constants.PROMPTS["tester"], "system")
        ], total_length=5)

        for cycle in range(max_cycles):
            observer(cycle, max_cycles)
            # Full collaboration logic here