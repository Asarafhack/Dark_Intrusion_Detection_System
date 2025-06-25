#!/bin/bash

echo "Starting DDoS Simulation Project..."
echo "==================================="
PS3='Choose an option: '
options=("Simulate DDoS Attack" "Detect DDoS Patterns" "Visualize Logs" "Activate Defense" "Exit")

select opt in "${options[@]}"
do
    case $opt in
        "Simulate DDoS Attack")
            python3 src/ddos_simulation.py
            ;;
        "Detect DDoS Patterns")
            python3 src/ddos_detection.py
            ;;
        "Visualize Logs")
            python3 src/visualize_logs.py
            ;;
        "Activate Defense")
            python3 src/defense_module.py
            ;;
        "Exit")
            break
            ;;
        *) echo "Invalid option $REPLY";;
    esac
done
