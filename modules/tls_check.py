import socket
import ssl
from datetime import datetime


def check_tls(url):

    target = (
        url.replace("https://", "")
        .replace("http://", "")
        .split("/")[0]
    )

    print("\n================================")
    print("       TLS/SSL CHECK")
    print("================================")

    print(f"[*] Target: {target}")

  
    # 1. Create SSL context
  

    context = ssl.create_default_context()

    try:

   
        # 2. Connect to HTTPS port 443
    

        with socket.create_connection(
            (target, 443),
            timeout=10
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=target
            ) as ssock:

               
                # 3. Get TLS version
             

                tls_version = ssock.version()
                print(f"\n[+] TLS Version: {tls_version}")

                
                # 4. Get certificate
               

                certificate = ssock.getpeercert()

                
                # 5. Certificate subject
                

                subject = dict(
                    item[0] for item in certificate["subject"]
                )

                common_name = subject.get(
                    "commonName",
                    "Unknown"
                )

                print(f"[+] Certificate Name: {common_name}")

                
                # 6. Certificate issuer
                

                issuer = dict(
                    item[0] for item in certificate["issuer"]
                )

                issuer_name = issuer.get(
                    "commonName",
                    "Unknown"
                )

                print(f"[+] Issuer: {issuer_name}")

          
                # 7. Certificate expiry
              

                expiry = certificate["notAfter"]

                expiry_date = datetime.strptime(
                    expiry,
                    "%b %d %H:%M:%S %Y %Z"
                )

                current_date = datetime.utcnow()

                print(
                    f"[+] Expiry Date: "
                    f"{expiry_date}"
                )

             
                # 8. Check expiry
                

                if expiry_date > current_date:

                    print("[OK] Certificate is valid")

                else:

                    print("[NOT OK] Certificate has expired")

    except ssl.SSLCertVerificationError as e:

        print("\n[NOT OK] SSL certificate verification failed")
        print(f"[!] Reason: {e}")

    except ssl.SSLError as e:

        print("\n[NOT OK] SSL/TLS error")
        print(f"[!] Reason: {e}")

    except socket.timeout:

        print("\n[NOT OK] Connection timed out")

    except ConnectionRefusedError:

        print("\n[NOT OK] Port 443 is closed")

    except Exception as e:

        print(f"\n[!] Error: {e}")