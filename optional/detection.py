import pandas as pd

def detect_ddos():
    log_file = "dataset/attack_logs.csv"
    detection_file = "dataset/detected_attacks.csv"
    
    try:
        logs = pd.read_csv(log_file)
    except FileNotFoundError:
        print("No attack logs found.")
        return

    # Detect potential DDoS by analyzing frequent requests to the same target
    attack_summary = logs.groupby("Target URL").size().reset_index(name="Packet Count")
    detected_attacks = attack_summary[attack_summary["Packet Count"] > 50]  # Threshold for detection
    
    if not detected_attacks.empty:
        print("\nDetected DDoS Attacks:")
        print(detected_attacks)
        detected_attacks.to_csv(detection_file, index=False)
        print(f"Details saved to {detection_file}")
    else:
        print("No DDoS patterns detected.")
