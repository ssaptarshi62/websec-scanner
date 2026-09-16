import requests

def check_exposed_files(url):
    if url.endswith('/'):
        url = url[:-1]

    sensitive_paths = [
        "/.git/config",
        "/.env",
        "/.DS_Store",
        "/wp-config.php.bak",
        "/config.php.bak",
        "/backup.zip",
        "/.htaccess",
        "/web.config",
        "/database.yml",
        "/.aws/credentials"
    ]

    print(f"\nChecking exposed files for {url} ...")

    for path in sensitive_paths:
        full_url = url + path
        try:
            response = requests.get(full_url, timeout=3)
            if response.status_code == 200:
                print(f"[-] EXPOSED: {full_url}")
            else:
                print(f"[+] Not exposed: {path} (status {response.status_code})")
        except requests.exceptions.RequestException:
            print(f"[!]  Could not check {path} (connection error)")