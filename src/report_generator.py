import os

LOG_FILE = "logs/attack_logs.csv"
REPORT_FILE = "reports/ddos_report.txt"

def generate_report():
    if not os.path.exists(LOG_FILE):
        print("No log file found. Run the DDoS simulation first.")
        return

    if not os.path.exists("reports"):
        os.makedirs("reports")

    with open(LOG_FILE, "r") as log_file, open(REPORT_FILE, "w") as report_file:
        lines = log_file.readlines()
        report_file.writelines(lines)

    print(f"Report generated at {REPORT_FILE}.")

if __name__ == "__main__":
    generate_report()
