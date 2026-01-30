from src.db import Database

db = Database()

def get_all_vms():
    return db.fetch_all()

def get_filtered_vms(provider=None, min_vcpu=None, min_memory=None, max_price=None, region=None):
    return db.fetch_filtered(provider, min_vcpu, min_memory, max_price, region)

def get_cheapest_vm():
    return db.fetch_cheapest()
