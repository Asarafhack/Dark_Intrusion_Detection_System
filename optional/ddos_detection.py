import pandas as pd

LOG_FILE = "logs/attack_logs.csv"

def detect_ddos():
    try:
        data = pd.read_csv(LOG_FILE)
        success_count = len(data[data["Status"] == "Success"])
        failure_count = len(data[data["Status"] == "Failure"])
        print("\nDDoS Detection Report:")
        print(f"Total Packets: {len(data)}")
        print(f"Success: {success_count}")
        print(f"Failure: {failure_count}")
        if failure_count > success_count:
            print("⚠️  Potential DDoS attack detected!")
        else:
            print("✅ No DDoS attack detected.")
    except FileNotFoundError:
        print("No log file found. Please simulate a DDoS attack first.")

if __name__ == "__main__":
    detect_ddos()
