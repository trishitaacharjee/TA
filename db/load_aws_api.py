import boto3
import json
import sqlite3

def fetch_aws_ec2_pricing():
    print("Fetching AWS EC2 pricing...")

    conn = sqlite3.connect("cloud_costs.db")
    cursor = conn.cursor()

    pricing = boto3.client("pricing", region_name="us-east-1")

    response = pricing.get_products(
        ServiceCode="AmazonEC2",
        Filters=[
            {"Type": "TERM_MATCH", "Field": "operatingSystem", "Value": "Linux"},
            {"Type": "TERM_MATCH", "Field": "tenancy", "Value": "Shared"},
            {"Type": "TERM_MATCH", "Field": "marketoption", "Value": "OnDemand"},
        ],
        MaxResults=20
    )

    inserted = 0

    for item in response["PriceList"]:
        data = json.loads(item)
        attributes = data["product"]["attributes"]

        instance_type = attributes.get("instanceType")
        vcpu = int(attributes.get("vcpu", 0))
        memory = attributes.get("memory", "0").replace(" GiB", "")
        region = attributes.get("location")

        for term in data["terms"]["OnDemand"].values():
            for dim in term["priceDimensions"].values():
                price = float(dim["pricePerUnit"].get("USD", 0))
                if price <= 0:
                    continue

                cursor.execute("""
                    INSERT INTO vm_costs
                    (provider, instance_type, vcpu, memory_gb, price_per_hour, region)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, ("AWS", instance_type, vcpu, float(memory), price, region))

                inserted += 1

    conn.commit()
    conn.close()

    print(f"AWS pricing loaded successfully. Rows inserted: {inserted}")

if __name__ == "__main__":
    fetch_aws_ec2_pricing()
