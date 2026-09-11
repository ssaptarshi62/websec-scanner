
import nmap


def check_openports(url):
    # Clean URL
    target = url.replace("https://", "").replace("http://", "").split("/")[0]

    print("\n================================")
    print("       Top 1000 ports scan")
    print("================================")

    print(f"\n[!] Target: {target}")
    print("[*] Scanning top 1000 common ports...")

    nm = nmap.PortScanner()

    try:
        # Run Nmap
        nm.scan(
            target,
            arguments= "-p 21,22,80,443,8080 -sV -T4 -Pn"
            # "--top-ports 1000 -sV -T4"
        )

        # Check if host was found
        if not nm.all_hosts():
            print("[-] Host is down or blocking the scan.")
            return

        # Read results
        for host in nm.all_hosts():

            for proto in nm[host].all_protocols():

                ports = nm[host][proto].keys()

                for port in sorted(ports):

                    state = nm[host][proto][port]["state"]
                    service = nm[host][proto][port]["name"]
                    version = nm[host][proto][port]["version"]

                    print(f"\nPort: {port}")
                    print(f"State: {state}")
                    print(f"Service: {service}")

                    if version:
                        print(f"Version: {version}")

    except Exception as e:
        print(f"[-] Error: {e}")   

   
