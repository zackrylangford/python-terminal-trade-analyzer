from rich.console import Console
from rich.table import Table

def visualize_data(analysis):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Metric")
    table.add_column("Value")

    for key, value in analysis.items():
        table.add_row(key.replace('_', ' ').capitalize(), str(value))
    
    console.print(table)

def visualize_success_by_time_of_day(success_by_time):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Time Slot")
    table.add_column("Success Rate (%)")
    table.add_column("Total Trades")

    all_time_slots = [f"{hour:02d} AM" for hour in range(1, 12)] + ["12 PM"] + [f"{hour:02d} PM" for hour in range(1, 12)]

    # Determine colors for top and bottom 3 success rates
    valid_success_rates = [(time_slot, stats['success_rate']) for time_slot, stats in success_by_time.items() if stats['success_rate'] is not None]
    sorted_success = sorted(valid_success_rates, key=lambda x: x[1], reverse=True)
    top_success = sorted_success[:3]
    bottom_success = sorted_success[-3:]

    for time_slot in all_time_slots:
        stats = success_by_time[time_slot]
        success_rate = stats['success_rate']
        total_trades = stats['total_trades']

        if success_rate is None:
            success_rate_str = "N/A"
            color = None
        else:
            success_rate_str = f"{success_rate:.2f}"
            if (time_slot, success_rate) in top_success:
                color = "green"
            elif (time_slot, success_rate) in bottom_success:
                color = "red"
            else:
                color = "yellow"

        table.add_row(time_slot, success_rate_str, str(total_trades), style=color)

    console.print(table)

if __name__ == "__main__":
    from . import analyze, fetch_data
    data = fetch_data.fetch_data()
    analysis = analyze.analyze_data(data)
    success_by_time = analyze.analyze_success_by_time_of_day(data)
    visualize_data(analysis)
    visualize_success_by_time_of_day(success_by_time)
