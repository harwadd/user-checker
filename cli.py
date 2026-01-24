from bootstrap import *  # noqa: F401

from rich import print
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, track
from rich.table import Table
from rich.panel import Panel

from sys import exit
from pathlib import Path
from src.checker import checker
import click

console = Console()
CONFIG_DIR = "src/config/"
BANNER_DIR = "src/assets/"

def load_usernames(file_path):
    # load usernames from a file
    if (Path(file_path).is_file()):
        with open(file_path, "r") as f:
            lines = f.read().splitlines()
            n_linhas = len(lines)
            print("[yellow]" + f"[!] {n_linhas} usernames loaded from {file_path}")
            return lines
    else:
        print("[red]" + f"[!] File not found: {file_path}")
        exit(1)

def load_banner(file_path):
    # load banner from a file
    if (Path(file_path).is_file()):
        with open(file_path, "r") as f:
            banner = f.read()
            return banner
    else:
        print("[red]" + f"[!] File not found: {file_path}")
        exit(1)



@click.command()
@click.option("--user", help="Username to check")
@click.option("--mode", help="Enter checking mode (hunter, sniper)")
@click.option("--time", type=int, help="Time between requests in seconds")
@click.option("--debug", is_flag=True, help="Enable debug mode")
@click.option("--proxy", is_flag=True, help="Use proxy for requests")
@click.option("--threads", type=int, help="Number of threads to use")
def main(debug, user, mode, proxy, threads, time):
    # display banner
    print("[green]" + load_banner(BANNER_DIR + "banner.txt"))
    print("[cyan][*] Loading usernames from file...\n")

    if user is not None:
        usernames = [user]
        print("[yellow][!] 1 username loaded from command line\n")
    else:
        usernames = load_usernames(CONFIG_DIR + "usernames.txt")

    print("[cyan]" + "[*] Starting username checks...\n")
    for username in usernames:
        checker(username=username, debug=debug, proxy=proxy)
        pass

if __name__ == "__main__":
    main()