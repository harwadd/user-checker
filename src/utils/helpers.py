import os, sys
import requests
import random


def randomize_user_agent():
    user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120 Safari/537.36 Edg/120.0.0.0"
        ]
    return random.choice(user_agents)

def randomize_proxy():
    port = random.randint(25000, 25002)

def generate_usernames(base_name, count):
    usernames = []
    for i in range(count):
        suffix = random.randint(100, 999)
        usernames.append(f"{base_name}{suffix}")
    return usernames

def save(filename: str, data: str) -> bool:
    with open("src/output/" + filename, "a") as f:
        f.write(data + "\n")
    print(f"[green]" + f"[+] Saved to src/output/{filename}")
    return True


def line(text: str = '----------------------------------'):
    return print(text)

def get_ip(proxy=None):
    response = requests.get("https://httpbin.org/ip", proxies=proxy, timeout=10)
    ip = response.json().get("origin")
    print(f"Current IP: {ip}")
    return ip