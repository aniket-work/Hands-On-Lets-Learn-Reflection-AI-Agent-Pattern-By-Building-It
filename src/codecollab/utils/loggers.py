from colorama import Fore, Style
import time

def observer(step: int, total_steps: int):
    emojis = ["❶","❷","❸","❹","❺"]
    border = f"{Fore.YELLOW}◇" * 50
    content = f"{Fore.WHITE} CYCLE {emojis[step]} {step+1}/{total_steps} "
    print(f"\n{border}\n{content.center(50, '◈')}\n{border}{Style.RESET_ALL}")
    time.sleep(0.3)