#!/root/domain-checker/venv/bin/python3.10
import requests
import subprocess
import os
import json
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv("/root/domain-checker/.env")

json_path = "domains.json"

def send_notification(domain: str):
    user_sid = os.getenv("USER_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    whatsapp_from = os.getenv("WHATSAPP_FROM")
    whatsapp_to = os.getenv("WHATSAPP_TO")
    client = Client(user_sid, auth_token)
    msg = f'Domain "{domain}" is now available'

    message = client.messages.create(from_=whatsapp_from, body=msg, to=whatsapp_to)


def check_domain(domain: str):
    result = subprocess.run(["whois", domain], capture_output=True, text=True)
    if "Status: free" in result.stdout:
        send_notification(domain)


with open(json_path, "r") as f:
    domains = json.load(f)

for i in domains["domains"]:
    check_domain(i)
