import sqlite3
import csv
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "cloud_costs.db")
CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "aws", "aws_vm_pricing.csv")

def load_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vm_costs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            provider TEXT,
            instance_type TEXT,
            vcpu INTEGER,
            memory_gb REAL,
            price_per_hour REAL
        )
    """)

    with open(CSV_PATH, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
                INSERT INTO vm_costs (provider, instance_type, vcpu, memory_gb, price_per_hour,region)
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
    print("AWS sample pricing data loaded successfully!")

if __name__ == "__main__":
    load_data()
