from datetime import datetime

# Raporu oluştur ve yaz
def generate_report(anomalies):
    with open("report.txt", "w") as file:
        file.write(f"Network Traffic Analysis Report\n")
        file.write(f"Generated on: {datetime.now()}\n\n")
        file.write("Anomalies Detected:\n")
        for anomaly in anomalies:
            file.write(f"{anomaly}\n")

# Örnek anormallikler listesi
anomalies = ["Port 80 has high traffic: 150 packets", "Port 443 has high traffic: 120 packets"]

# Raporu oluştur
generate_report(anomalies)