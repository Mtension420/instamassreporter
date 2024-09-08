from instapy import InstaPy
import threading

def read_credentials(file_path):
    credentials = []
    with open(file_path, 'r') as file:
        for line in file:
            username, password = line.strip().split(':')
            credentials.append({"username": username, "password": password})
    return credentials

def read_proxies(file_path):
    proxies = []
    with open(file_path, 'r') as file:
        for line in file:
            proxy = line.strip()
            proxies.append(proxy)
    return proxies

def login_and_report(user, proxy, target_username):
    try:
        session = InstaPy(username=user["username"], password=user["password"])
        
        # Set the proxy for the session
        session.set_proxies(proxy_address=proxy, proxy_chrome_extension=False)
        
        # Logging in
        session.login()
        
        # Reporting the user
        session.report_user(target_username, "spam")
        
        # Logging out
        session.end()
        print(f"Reported {target_username} with {user['username']}")
    except Exception as e:
        print(f"Failed for {user['username']} with proxy {proxy}: {str(e)}")

def main():
    credentials_file = input("Enter the path to the TXT file with Instagram credentials (username:password): ")
    proxies_file = input("Enter the path to the TXT file with proxies (http://proxy:port): ")
    target_username = input("Enter the username to report: ")

    credentials = read_credentials(credentials_file)
    proxies = read_proxies(proxies_file)

    threads = []
    for i, user in enumerate(credentials):
        proxy = proxies[i % len(proxies)]  # Cycle through proxies
        t = threading.Thread(target=login_and_report, args=(user, proxy, target_username))
        t.start()
        threads.append(t)

    # Join all threads to ensure they complete
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
