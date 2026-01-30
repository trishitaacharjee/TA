import sqlite3

class Database:
    def __init__(self, path="db/cloud_costs.db"):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

    def fetch_all(self):
        self.cursor.execute("""
            SELECT provider, instance_type, vcpu, memory_gb, price_per_hour, region
            FROM vm_costs
        """)
        return self.cursor.fetchall()

    def fetch_filtered(self, provider=None, min_vcpu=None, min_memory=None, max_price=None, region=None):
        query = """
            SELECT provider, instance_type, vcpu, memory_gb, price_per_hour, region
            FROM vm_costs WHERE 1=1
        """
        params = []

        if provider:
            query += " AND provider = ?"
            params.append(provider)

        if min_vcpu:
            query += " AND vcpu >= ?"
            params.append(min_vcpu)

        if min_memory:
            query += " AND memory_gb >= ?"
            params.append(min_memory)

        if max_price:
            query += " AND price_per_hour <= ?"
            params.append(max_price)

        if region:
            query += " AND region = ?"
            params.append(region)

        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_cheapest(self):
        self.cursor.execute("""
            SELECT provider, instance_type, vcpu, memory_gb, price_per_hour, region
            FROM vm_costs
            ORDER BY price_per_hour ASC LIMIT 1
        """)
        return self.cursor.fetchone()
