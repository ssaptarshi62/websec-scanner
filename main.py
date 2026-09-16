from modules.header_check import check_headers
from modules.port_scanner import check_openports
from modules.tls_check import check_tls
from modules.exposed_files import check_exposed_files


def run_all_checks(url):
    check_headers(url)



def main():
    url = input("Enter the website URL (include http:// or https://): ")

    while True:
        print("\nChoose a check to run:")
        print("1. Header Check")
        print("2. Open ports check")
        print("3. TLS/SSL Check")
        print("4. Exposed File Check")
        print("5. Exit")
  
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            check_headers(url)

        elif choice == "2":
            check_openports(url)

        elif choice == "3":
            check_tls(url)

        elif choice == "4":
            check_exposed_files(url)

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


main()