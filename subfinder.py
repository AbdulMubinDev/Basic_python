import requests

def subdomain_finder(domain, wordlist_path, timeout_time):
    with open(wordlist_path, 'r') as file:
        subdomains = file.read().splitlines()
        found_subdomains = []

        for sub in subdomains:
            url = f"{sub}.{domain}"
            for scheme in ["http://", "https://"]:
                try:
                    response = requests.get(f"{scheme}{url}", timeout=timeout_time)
                    if response.status_code in [200, 301, 302, 403]:
                        found_subdomains.append(f"{scheme}{url}")
                        print(f"[+] Found subdomain: {scheme}{url}")
                        break  # Stop after first successful scheme
                except requests.RequestException:
                    pass
        return found_subdomains

if __name__ == "__main__":
    domain = input("Enter the main domain (e.g. example.com): ")
    wordlist_path = input("Enter the path to your wordlist file: ")
    timeout_time = int(input("Enter the timeout time in seconds: "))
    if not domain or not wordlist_path or not timeout_time:
        print("All inputs are required.")
        exit(1)
    if not wordlist_path.endswith('.txt'):
        print("Please provide a valid wordlist file with a .txt extension.")
        exit(1)
    if timeout_time <= 0:
        print("Timeout time must be a positive integer.")
        exit(1)
    if not (domain.endswith('.com') or domain.endswith('.org') or domain.endswith('.net')):
        print("Please provide a valid domain ending with .com, .org, or .net.")
        exit(1)
    print(f"Starting subdomain scan for {domain} using wordlist {wordlist_path} with a timeout of {timeout_time} seconds...")
    found = subdomain_finder(domain, wordlist_path, timeout_time)
    print("\nScan complete. Found subdomains:")
    for sub in found:
        print(sub)