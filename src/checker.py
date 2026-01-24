import os, sys
import requests
import random
import cloudscraper

import json

from services import discord

proxy = f"http://127.0.0.1:25000"
proxies = {"http": proxy, "https": proxy}

def checker(username, repeat=False, debug=False, proxy=False):
    is_available = discord(username, proxy=proxy)
    print(f"Checked username: {username}, Available: {is_available}")
    return is_available

