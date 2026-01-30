import sqlite3
import csv
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "cloud_costs.db")
CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "gcp", "gcp_vm_pricing.csv")

def load_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open(CSV_PATH, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute("""
                INSERT INTO vm_costs (provider, instance_type, vcpu, memory_gb, price_per_hour, region)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                row["provider"],
                row["instance_type"],
                row["vcpu"],
                row["memory_gb"],
                row["price_per_hour"],
                row["region"]
            ))

    conn.commit()
    conn.close()
    print("GCP sample data loaded.")

if __name__ == "__main__":
    load_data()
