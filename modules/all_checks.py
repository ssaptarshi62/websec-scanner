from modules.header_check import check_headers
from modules.port_scanner import check_openports
from modules.tls_check import check_tls
from modules.exposed_files import check_exposed_files

def run_all_checks(url):
    print(f"Target: {url}")
    check_headers(url) 
    check_openports(url)
    check_tls(url)         
    check_exposed_files(url) 
    run_all_checks(url) 

