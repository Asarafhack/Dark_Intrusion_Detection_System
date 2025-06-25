import pandas as pd
import matplotlib.pyplot as plt

def visualize_logs():
    log_file = "dataset/attack_logs.csv"
    try:
        logs = pd.read_csv(log_file)
    except FileNotFoundError:
        print("No attack logs found to visualize.")
        return
    
    # Visualize the number of packets sent to each target
    attack_summary = logs.groupby("Target URL").size().reset_index(name="Packet Count")
    plt.bar(attack_summary["Target URL"], attack_summary["Packet Count"], color='skyblue')
    plt.title("DDoS Attack Summary")
    plt.xlabel("Target URL")
    plt.ylabel("Number of Packets")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
