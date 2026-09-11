import requests

def check_headers(url):

    important_headers = [
        "Strict-Transport-Security",
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Referrer-Policy",
            "Permissions-Policy"
    ]


    response = requests.get(url)

    headers = response.headers


    for header in important_headers:
        if header in headers:
            print(f"[+] , {header} is present ")
        else:
            print(f"[-], {header} is not present ")

