import time
import csv
import os
import ipaddress
from collections import Counter

# File Paths
LOG_FILE = "logs/request_logs.csv"
BLOCKED_IP_FILE = "logs/blocked_ips.txt"

# Detection Parameters
BLOCK_THRESHOLD = 1000  # Requests per IP within detection window
DETECTION_WINDOW = 1  # Seconds

# Ensure logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

def load_logs():
    """Load logs from the CSV file."""
    if not os.path.exists(LOG_FILE):
        print("No log file found. Please start monitoring first.")
        return []

    logs = []
    with open(LOG_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            try:
                logs.append({
                    "timestamp": int(row[0]),
                    "ip": row[1],
                    "status": row[2]
                })
            except (ValueError, IndexError):
                continue
    return logs

def detect_ddos():
    """Detect potential DDoS attacks."""
    logs = load_logs()
    if not logs:
        return

    print("\n🔍 Analyzing logs for DDoS patterns...")
    time.sleep(1)

    current_time = int(time.time())
    window_start = current_time - DETECTION_WINDOW

    # Filter logs within the detection window
    recent_logs = [log for log in logs if window_start <= log["timestamp"] <= current_time]
    ip_counts = Counter(log["ip"] for log in recent_logs)

    print("\n📊 DDoS Detection Report:")
    print("=======================")
    for ip, count in ip_counts.items():
        print(f"IP: {ip}, Requests: {count}")
        if count > BLOCK_THRESHOLD:
            block_ip(ip)

    if any(count > BLOCK_THRESHOLD for count in ip_counts.values()):
        print("⚠️  DDoS attack detected! Blocking malicious IPs.")
    else:
        print("✅  No significant DDoS patterns detected.")

def block_ip(ip):
    """Block the given IP address."""
    if not is_valid_ip(ip):
        print(f"❌ Invalid IP address: {ip}")
        return

    with open(BLOCKED_IP_FILE, "a") as file:
        file.write(f"{ip}\n")

    print(f"🚫 IP {ip} has been blocked!")

def is_valid_ip(ip):
    """Check if an IP address is valid."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def view_blocked_ips():
    """View all blocked IPs."""
    if not os.path.exists(BLOCKED_IP_FILE):
        print("No blocked IPs yet.")
        return

    print("\n🚫 Blocked IPs:")
    print("============")
    with open(BLOCKED_IP_FILE, "r") as file:
        for line in file:
            print(line.strip())

def generate_report():
    """Generate a summary report of blocked IPs and detected patterns."""
    logs = load_logs()
    if not logs:
        print("No logs to generate a report.")
        return

    current_time = int(time.time())
    window_start = current_time - DETECTION_WINDOW
    recent_logs = [log for log in logs if window_start <= log["timestamp"] <= current_time]
    ip_counts = Counter(log["ip"] for log in recent_logs)

    with open("DDoS_Report.txt", "w") as report_file:
        report_file.write("DDoS Attack Detection Report\n")
        report_file.write("===========================\n\n")
        for ip, count in ip_counts.items():
            report_file.write(f"IP: {ip}, Requests: {count}\n")
            if count > BLOCK_THRESHOLD:
                report_file.write(f"  Status: Blocked (Threshold exceeded)\n")
            else:
                report_file.write(f"  Status: No action required\n")

    print("✅ DDoS Detection Report generated successfully: DDoS_Report.txt")

if __name__ == "__main__":
    print("🛡️ Advanced DDoS Detection System")
    while True:
        print("""
        1. Analyze Logs
        2. View Blocked IPs
        3. Generate DDoS Report
        4. Exit
        """)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            detect_ddos()
        elif choice == "2":
            view_blocked_ips()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            print("Exiting... 🛑")
            break
        else:
            print("Invalid option. Please try again.")
