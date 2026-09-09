import requests

def check_headers(url):

    important_headers = [
        "Strict-Transport-Security",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Content-Security-Policy"
    ]


    response = requests.get(url)

    headers = response.headers


    for header in important_headers:
        if header in headers:
            print(f"ok , {header} is present ")
        else:
            print(f"not ok, {header} is not present ")

check_headers("http://testfire.net/")