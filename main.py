from scanner.http_scanner import scan_url
from scanner.report import generate_report

def load_urls_from_file(filename="urls.txt"):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]

def main():
    urls = load_urls_from_file()
    print(f"[!] Mulai scan {len(urls)} URL...")

    scan_results = []
    for url in urls:
        print(f"🔍 Scanning: {url}")
        result = scan_url(url)
        scan_results.append(result)
    
    generate_report(scan_results)

if __name__ == "__main__":
    main()
