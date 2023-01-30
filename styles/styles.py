from colorama import Fore, Back, Style


def title_text(text):
    return print(Fore.YELLOW + Back.LIGHTBLACK_EX + text + Style.RESET_ALL)


def option_text(text):
    return print(Fore.BLUE + text + Style.RESET_ALL)


def error_text(text):
    return print(Fore.RED + text + Style.RESET_ALL)
