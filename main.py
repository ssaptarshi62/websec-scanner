from modules.header_check import check_headers


def run_all_checks(url):
    check_headers(url)



def main():
    url = input("Enter the website URL (include http:// or https://): ")

    while True:
        print("\nChoose a check to run:=>")
        print("1. Header Check")
        print("2. TLS/SSL Check")
        print("3. Exposed File Check")
        print("4. Dependency Vulnerability Scan")
        print("5. Run All Checks (Full Report)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            check_headers(url)

        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


main()