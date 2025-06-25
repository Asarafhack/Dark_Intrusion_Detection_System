import os
import sys
from time import sleep
from src.ddos_simulation import simulate_ddos
from src.ddos_detection import detect_ddos
from src.visualizer import visualize_logs
from src.report_generator import generate_report
from colorama import Fore, Back, Style

# Banner in Green and Red
banner = '''
  ___                       __    ___  _____   _   _      _   _                 _                  _     _            
 / _ \                     / _|  / _ \|_   _| | \ | |    | | | |               | |                | |   | |           
/ /_\ \___  __ _ _ __ __ _| |_  / /_\ \ | |   |  \| | ___| |_| |__  _   _ _ __ | |_ ___ _ __    __| | __| | ___  ___  
|  _  / __|/ _` | '__/ _` |  _| |  _  | | |   | . ` |/ _ \ __| '_ \| | | | '_ \| __/ _ \ '__|  / _` |/ _` |/ _ \/ __| 
| | | \__ \ (_| | | | (_| | |   | | | |_| |_  | |\  |  __/ |_| | | | |_| | | | | ||  __/ |    | (_| | (_| | (_) \__ \ 
\_| |_/___/\__,_|_|  \__,_|_|   \_| |_/\___/  \_| \_/\___|\__|_| |_|\__,_|_| |_|\__\___|_|     \__,_|\__,_|\___/|___/ 
'''

def print_banner():
    # Print the banner with green and red color scheme
    print(Fore.GREEN + banner)
    print(Fore.RED + "Welcome to your Python Application!")
    print(Style.RESET_ALL)

# Your code functionality starts here
def main():
    print_banner()

def green_border_text(text):
    """Wrap text with a green border."""
    border = f"\033[92m{'=' * (len(text) + 4)}\033[0m"
    print(border)
    print(f"\033[92m| {text} |\033[0m")
    print(border)

def red_border_text(text):
    """Wrap text with a red border."""
    border = f"\033[91m{'=' * (len(text) + 4)}\033[0m"
    print(border)
    print(f"\033[91m| {text} |\033[0m")
    print(border)

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_hacker_banner():
    """Display the hacker-themed ASCII art."""
    clear_screen()
    print("\033[92m" + "=" * 60 + "\033[0m")
    print(r"""
        \033[92m
          █████╗ ███████╗ █████╗ ██████╗  █████╗ ███████╗
         ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
         ███████║█████╗  ███████║██████╔╝███████║███████╗
         ██╔══██║██╔══╝  ██╔══██║██╔═══╝ ██╔══██║╚════██║
         ██║  ██║███████╗██║  ██║██║     ██║  ██║███████║
         ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝

            ASARAF AI DDoS TERMINAL - POWERED BY YOUR EXPERTISE
                    AI IN ACTION   --  2717
    """)
    print("\033[92m" + "=" * 60 + "\033[0m")
    sleep(1)

def loading_animation(text):
    """Display a loading animation."""
    for i in range(3):
        sys.stdout.write(f"\r\033[93m{text} {'.' * (i + 1)}\033[0m")
        sys.stdout.flush()
        sleep(0.5)
    print("\r\033[92m" + " " * 50 + "\033[0m", end="\r")

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        display_hacker_banner()
        print("""\033[92m
        === ASARAF AI DDoS TERMINAL ===
        \033[0m
        1. 💣 Simulate DDoS Attack
        2. 🔍 Detect DDoS Patterns
        3. 📊 Visualize Logs
        4. 📝 Generate Report
        5. 🚪 Exit
        """)
        choice = input("\033[96mChoose an option: \033[0m")

        if choice == "1":
            loading_animation("Simulating DDoS Attack")
            simulate_ddos()
            input("\033[92mPress Enter to return to the menu.\033[0m")
        elif choice == "2":
            loading_animation("Detecting DDoS Patterns")
            detect_ddos()
            input("\033[92mPress Enter to return to the menu.\033[0m")
        elif choice == "3":
            loading_animation("Visualizing Logs")
            visualize_logs()
            input("\033[92mPress Enter to return to the menu.\033[0m")
        elif choice == "4":
            filename = input("\033[96mEnter report filename (e.g., report.pdf): \033[0m")
            loading_animation("Generating Report")
            generate_report(filename)
            green_border_text("Report generated successfully!")
            input("\033[92mPress Enter to return to the menu.\033[0m")
        elif choice == "5":
            red_border_text("Goodbye! Stay Secure with ASARAF AI!")
            sleep(2)
            sys.exit()
        else:
            red_border_text("Invalid choice! Please try again.")
            sleep(2)

if __name__ == "__main__":
    main_menu()
