from colorama import Fore, Style
from dotenv import load_dotenv
from codecollab.core.orchestrator import DevTestOrchestrator
from codecollab.core.agents import DeveloperAgent, TesterAgent
from codecollab.utils.helpers import load_template

load_dotenv()


def main():
    # Initialize agents
    developer = DeveloperAgent()
    tester = TesterAgent()

    # Load system prompts
    dev_prompt = load_template("developer.j2")
    test_prompt = load_template("tester.j2")

    # Create orchestrator
    orchestrator = DevTestOrchestrator(
        developer=developer,
        tester=tester,
        dev_prompt=dev_prompt,
        test_prompt=test_prompt
    )

    # Run collaboration cycle
    result = orchestrator.run_cycle(
        user_request="Implement Python AVL tree with rotation methods",
        max_cycles=4
    )

    print(f"\n{Fore.CYAN}🚀 FINAL RESULT:{Style.RESET_ALL}")
    print(result)


if __name__ == "__main__":
    main()