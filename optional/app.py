from attack_simulation import simulate_ddos_attack
from detection import detect_ddos
from visualization import visualize_logs

def display_menu():
    print("\nDDoS Simulation and Detection")
    print("=" * 30)
    print("1. Simulate DDoS Attack")
    print("2. Detect DDoS Patterns")
    print("3. Visualize Logs")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            target_url = input("Enter the target URL: ").strip()
            num_packets = int(input("Enter the number of packets to send: ").strip())
            delay = float(input("Enter the delay between packets (seconds): ").strip())
            simulate_ddos_attack(target_url, num_packets, delay)
        
        elif choice == "2":
            detect_ddos()
        
        elif choice == "3":
            visualize_logs()
        
        elif choice == "4":
            print("Exiting application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
