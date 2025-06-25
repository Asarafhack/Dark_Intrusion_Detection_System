import time
import requests
import csv

def simulate_ddos_attack(target_url, num_packets, delay):
    log_file = "dataset/attack_logs.csv"
    
    # Ensure logs directory exists
    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Target URL", "Packet Number", "Status"])
    
    print(f"Starting simulated DDoS attack on {target_url}...")
    for i in range(1, num_packets + 1):
        try:
            response = requests.get(target_url)
            status = f"Success (HTTP {response.status_code})"
        except Exception as e:
            status = f"Failed ({str(e)})"
        
        # Log the packet details
        with open(log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), target_url, i, status])
        
        print(f"Packet {i}: {status}")
        time.sleep(delay)
    print(f"Simulated DDoS attack completed. Logs saved to {log_file}")
