from bootstrap import *  # noqa: F401

from rich import print
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, track
from rich.table import Table
from rich.panel import Panel

from sys import exit
from pathlib import Path
from src.checker import check_username
import click




console = Console()

banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣤⡤⣤⠤⣾⣿⣽⣿⣿⠁⠀⠀⠀SnipeX⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣀⣠⣤⣤⣀⠀⣀⣼⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠆
⣼⣿⣿⣿⣿⣧⣤⣿⠿⠉⠿⠿⠿⠛⠛⠛⠛⠛⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠿⠿⠛⠛⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡆by Harwad⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
----------------------------------
|   GitHub:
----------------------------------
"""

CONFIG_DIR = "src/config/"
caminho = Path(CONFIG_DIR + "usernames.txt")


def load(file_path):
    if (caminho.is_file(), caminho.exists()) == (True, True):
        with open(file_path, "r") as f:
            lines = f.read().splitlines()
            n_linhas = len(lines)
            print("[yellow]" + f"[!] {n_linhas} usernames loaded from {file_path}\n")
            return lines
    else:
        print("[red]" + f"[!] File not found: {file_path}")
        exit(1)

    


@click.command()
@click.option("--user", help="Username to check")
@click.option("--debug", is_flag=True, help="Enable debug mode")
@click.option("--repeat", is_flag=True, help="Check a username constantly until interrupted")
def main(debug, user, repeat):
    print("[bold green]" + banner)
    print("[cyan][*] Loading usernames from file...\n")

    if user is not None:
        usernames = [user]
        print("[yellow][!] 1 username loaded from command line\n")
    else:
        usernames = load(caminho)

    print("Usernames to check:")
    for username in usernames:
        print(f"- {username}")

    print("[cyan]" + "[*] Starting username checks...\n")
    for username in usernames:
        check_username(username=username, repeat=repeat, debug=debug)
        pass




if __name__ == "__main__":
    main()