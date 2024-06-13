# main.py

from . import fetch_data
from . import analyze
from . import visualize

def welcome_screen():
    print("Welcome to Trading Stats Analyzer")
    print("=================================")
    print("Please select a report to generate:")
    print("1. Total Trades")
    print("2. Total Profit/Loss")
    print("3. Average Trade Duration")
    print("4. Win Rate")
    print("5. All Metrics")
    print("6. Refresh Data")
    print("0. Exit")

def main():
    while True:
        welcome_screen()
        choice = input("Enter your choice (0-6): ")

        if choice == '6':
            fetch_data.fetch_data()
            print("Data refreshed successfully.")
            continue

        data = analyze.read_from_csv()
        analysis = analyze.analyze_data(data)

        if choice == '1':
            visualize.visualize_data({"total_trades": analysis["total_trades"]})
        elif choice == '2':
            visualize.visualize_data({"total_profit_loss": analysis["total_profit_loss"]})
        elif choice == '3':
            visualize.visualize_data({"avg_duration": analysis["avg_duration"]})
        elif choice == '4':
            visualize.visualize_data({"win_rate": analysis["win_rate"]})
        elif choice == '5':
            visualize.visualize_data(analysis)
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
