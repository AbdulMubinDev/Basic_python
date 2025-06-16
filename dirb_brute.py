import requests

def dirb_brute (base_url, wordlist_path):
    
    try:
        with open(wordlist_path, 'r') as file:
            words = [line for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: The wordlist file {wordlist_path} was not found...")
        return
    

    print(f"starting brute force attack on {base_url} with wordlist {wordlist_path}...")
    for word in words: 
        url = f"{base_url.rstrip('/')}/{word.strip()}"
        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200: 
                print(f"Found: {url} (Status Code: {response.status_code})")
            elif response.status_code == 403:
                print(f"Forbidden: {url} (Status Code: {response.status_code})")
        except requests.RequestException as e: 
            print(f"Error accessing {url}: {e}")
    print("Brute force attack completed.")


if __name__ == "__main__":
    target_url = input("Enter the target URL (e.g., http://example.com): ").strip()
    wordlist_file = input("Enter the path to the wordlist file: ").strip()

    dirb_brute(target_url, wordlist_file)
    