import requests

def scan_url(url):
    try:
        response = requests.get(url, timeout=5)
        return {
            "url": url,
            "status_code": response.status_code,
            "reason": response.reason
        }
    except requests.RequestException as e:
        return {
            "url": url,
            "status_code": None,
            "reason": str(e)
        }
