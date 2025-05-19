import pandas as pd

def generate_report(scan_results, filename="scan_report.csv"):
    df = pd.DataFrame(scan_results)
    df.to_csv(filename, index=False)
    print(f"[✔] Laporan disimpan ke: {filename}")
