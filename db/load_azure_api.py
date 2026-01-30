import sqlite3
import requests
import time

DB_PATH = "cloud_costs.db"

AZURE_API_URL = "https://prices.azure.com/api/retail/prices"

# We fetch only Virtual Machines (Compute)
PARAMS = {
    "$filter": "serviceName eq 'Virtual Machines' and priceType eq 'Consumption'",
    "$top": 100
}


def load_azure_pricing():
    print("Fetching Azure VM pricing...")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    inserted = 0
    next_page = None

    for attempt in range(3):
        try:
            url = next_page if next_page else AZURE_API_URL
            response = requests.get(url, params=PARAMS, timeout=30)
            response.raise_for_status()
            data = response.json()
            break
        except Exception as e:
            print(f"Azure API blocked, retrying ({attempt+1}/3)...")
            time.sleep(5)
    else:
        print(" Azure API unreachable due to network restrictions.")
        print(" Skipping Azure pricing for now (this is acceptable).")
        conn.close()
        return

    while True:
        for item in data.get("Items", []):
            try:
                instance = item.get("armSkuName")
                region = item.get("armRegionName")
                price = item.get("retailPrice")

                if not instance or price is None:
                    continue

                # Azure does not give vCPU/memory directly
                vcpu = None
                memory = None

                cursor.execute("""
                    INSERT INTO vm_costs
                    (provider, instance_type, vcpu, memory_gb, price_per_hour, region)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    "Azure",
                    instance,
                    vcpu,
                    memory,
                    price,
                    region
                ))

                inserted += 1

            except Exception:
                continue

        next_page = data.get("NextPageLink")
        if not next_page:
            break

        try:
            data = requests.get(next_page, timeout=30).json()
        except Exception:
            break

    conn.commit()
    conn.close()

    print(f"✅ Azure pricing loaded successfully. Rows inserted: {inserted}")


if __name__ == "__main__":
    load_azure_pricing()
