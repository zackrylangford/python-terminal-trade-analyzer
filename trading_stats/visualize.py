# visualize.py

from rich.console import Console
from rich.table import Table

def visualize_data(analysis):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Metric")
    table.add_column("Value")

    for key, value in analysis.items():
        table.add_row(key, str(value))
    
    console.print(table)

if __name__ == "__main__":
    from . import analyze, fetch_data
    data = fetch_data.fetch_data()
    analysis = analyze.analyze_data(data)
    visualize_data(analysis)
