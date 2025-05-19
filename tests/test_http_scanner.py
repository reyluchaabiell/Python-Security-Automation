from scanner.http_scanner import scan_url

def test_scan_valid_url():
    result = scan_url("https://httpbin.org/status/200")
    assert result["status_code"] == 200
    assert "url" in result

def test_scan_invalid_url():
    result = scan_url("https://invalid.thisdoesnotexist")
    # Kalau error, status_code harus None, dan ada pesan di "reason"
    assert result["status_code"] is None
    assert "reason" in result and result["reason"] != ""
