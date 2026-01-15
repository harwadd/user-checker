import os, sys
import requests
from rich import print
import random
import cloudscraper

from utils.helpers import randomize_user_agent



def discord(username):
    #get_ip()
    api = f"https://discord.com/api/v9/unique-username/username-attempt-unauthed"

    headers = {
                'User-Agent': randomize_user_agent(),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
            }
    
    for _ in range(3):  # Retry up to 3 times
        proxy = f"http://127.0.0.1:{random.randint(25000, 25002)}"
        proxies = {"http": proxy, "https": proxy}
        print(f"Checking Discord for username: {username}")
        response = requests.post(
                api, 
                headers=headers, 
                json={ "username": username }, 
                timeout=5,
                proxies=proxies
            )
        print(proxy)
        print(response.text)
        if response.status_code == 200:
            data = response.json()
            if data and data.get("taken") == False:
                print(f"[green][+] Username {username} is available on Discord[/green]")
                return True
            
        if response.status_code == 429:
            print("[yellow][!] Rate limited, retrying...[/yellow]")
            continue  # Retry on rate limit

        print(f"Username {username} is taken on Discord")
        
        return False