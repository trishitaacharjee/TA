import csv
import os

def export_to_csv(data, filename="vm_results.csv"):
    """Save VM result rows into a CSV file under output/ folder."""

    os.makedirs("output", exist_ok=True)
    filepath = os.path.join("output", filename)

    headers = ["provider", "instance_type", "vcpu", "memory_gb", "price_per_hour", "region"]

    with open(filepath, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

    return filepath
