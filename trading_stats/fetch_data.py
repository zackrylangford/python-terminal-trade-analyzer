# fetch_data.py

import requests
import csv
import os

api_endpoint = "https://adhp0jlvy5.execute-api.us-east-1.amazonaws.com/default/visualize-trade-data"
csv_file = os.path.join(os.path.dirname(__file__), 'data.csv')

def fetch_data():
    response = requests.get(api_endpoint)
    if response.status_code == 200:
        data = response.json()
        save_to_csv(data)
        return data
    else:
        raise Exception("Failed to fetch data")

def save_to_csv(data):
    keys = data[0].keys()
    with open(csv_file, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

if __name__ == "__main__":
    data = fetch_data()
    print(data)
