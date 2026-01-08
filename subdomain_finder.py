import requests

def find_subdomains(domain, list_of_subdomains):
    print(f"--- Scanning {domain} for Subdomains ---")
    for sub in list_of_subdomains:
        url = f"http://{sub}.{domain}"
        try:
            requests.get(url, timeout=2)
            print(f"[FOUND] {url}")
        except requests.ConnectionError:
            pass

# Example usage with a tiny list
subs = ['dev', 'staging', 'api', 'admin', 'test', 'mail']
find_subdomains("google.com", subs) # Uncomment to run