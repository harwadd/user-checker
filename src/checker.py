import os, sys
import requests
import random
import cloudscraper

from services import discord

proxy = f"http://127.0.0.1:25000"
proxies = {"http": proxy, "https": proxy}

def check_username(username, repeat=False, debug=False):
    is_available = discord(username)
    print(f"Checked username: {username}, Available: {is_available}")
    return is_available

