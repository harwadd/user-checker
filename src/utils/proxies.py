import os, sys
import requests
import json
from pathlib import Path

def load_proxies(file_path):
    # load proxies from a file
    if (Path(file_path).is_file()):
        with open(file_path, "r") as f:
            return json.load(f)
    else:
        print("[red]" + f"[!] File not found: {file_path}")

def configure_proxy(proxy_config):
    if proxy_config["host"] and proxy_config["port"]:
        proxy_auth = ""
        if proxy_config["user"] and proxy_config["pass"]:
            proxy_auth = f"{proxy_config['user']}:{proxy_config['pass']}@"
            proxy_url = f"http://{proxy_auth}{proxy_config['host']}:{proxy_config['port']}"
        else:
            proxy_url = f"http://{proxy_config['host']}:{proxy_config['port']}"
        return proxy_url
    return None

def get_proxies():
    proxy_config = load_proxies("src/config/proxies.json")
    proxy_url = configure_proxy(proxy_config)
    return proxy_url

def proxy_dict(proxy):
    return {
        "http": proxy,
        "https": proxy,
    }