import matplotlib.pyplot as plt
import csv

LOG_FILE = "logs/attack_logs.csv"

def visualize_logs():
    if not os.path.exists(LOG_FILE):
        print("No log file found. Run the DDoS simulation first.")
        return

    packets = []
    statuses = {"Success": 0, "Failure": 0}

    with open(LOG_FILE, "r") as log_file:
        reader = csv.DictReader(log_file)
        for row in reader:
            packets.append(row)
            statuses[row["Status"]] += 1

    # Bar chart for Success vs Failure
    plt.bar(statuses.keys(), statuses.values(), color=["green", "red"])
    plt.title("DDoS Attack Simulation Results")
    plt.xlabel("Status")
    plt.ylabel("Number of Packets")
    plt.show()

if __name__ == "__main__":
    visualize_logs()
