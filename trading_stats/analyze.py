import csv
import os
import pandas as pd
from collections import defaultdict

csv_file = os.path.join(os.path.dirname(__file__), 'data.csv')

def read_from_csv():
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

def analyze_data(data):
    total_trades = len(data)
    total_profit_loss = sum(float(trade['TotalPnL']) for trade in data)
    total_duration = sum((pd.to_datetime(trade['ExitedAt']) - pd.to_datetime(trade['EnteredAt'])).total_seconds() for trade in data)
    avg_duration = total_duration / total_trades if total_trades > 0 else 0
    wins = sum(1 for trade in data if float(trade['TotalPnL']) > 0)
    win_rate = (wins / total_trades) * 100 if total_trades > 0 else 0

    avg_profit_per_trade = total_profit_loss / total_trades if total_trades > 0 else 0
    max_profit = max(float(trade['TotalPnL']) for trade in data)
    max_loss = min(float(trade['TotalPnL']) for trade in data)

    return {
        "total_trades": total_trades,
        "total_profit_loss": total_profit_loss,
        "avg_duration": avg_duration,
        "win_rate": win_rate,
        "avg_profit_per_trade": avg_profit_per_trade,
        "max_profit": max_profit,
        "max_loss": max_loss
    }

def analyze_success_by_time_of_day(data):
    time_slots = defaultdict(lambda: {'wins': 0, 'losses': 0, 'total': 0})

    for trade in data:
        entry_time = pd.to_datetime(trade['EnteredAt'])
        time_slot = entry_time.strftime('%I %p')  # 12-hour format with AM/PM
        if float(trade['TotalPnL']) > 0:
            time_slots[time_slot]['wins'] += 1
        else:
            time_slots[time_slot]['losses'] += 1
        time_slots[time_slot]['total'] += 1

    all_time_slots = [f"{hour:02d} AM" for hour in range(1, 12)] + ["12 PM"] + [f"{hour:02d} PM" for hour in range(1, 12)]

    success_rate_by_time = {}
    for time_slot in all_time_slots:
        results = time_slots[time_slot]
        total_trades = results['total']
        if total_trades > 0:
            success_rate = (results['wins'] / total_trades) * 100
        else:
            success_rate = None
        success_rate_by_time[time_slot] = {
            'success_rate': success_rate,
            'total_trades': total_trades
        }

    return success_rate_by_time

if __name__ == "__main__":
    data = read_from_csv()
    analysis = analyze_data(data)
    success_by_time = analyze_success_by_time_of_day(data)
    print(analysis)
    print(success_by_time)
