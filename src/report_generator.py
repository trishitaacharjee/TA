import csv
import os
from datetime import datetime
from src.cost_analyzer import (
    get_all_vms,
    get_filtered_vms,
    get_cheapest_vm
)

EXPORT_DIR = "exports"


def ensure_export_dir():
    if not os.path.exists(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)


def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def export_all_vms():
    ensure_export_dir()
    filename = f"{EXPORT_DIR}/all_vm_pricing_{timestamp()}.csv"
    rows = get_all_vms()
    write_csv(filename, rows)
    return filename


def export_filtered_vms(provider=None, region=None, max_price=None):
    ensure_export_dir()
    filename = f"{EXPORT_DIR}/filtered_vm_pricing_{timestamp()}.csv"
    rows = get_filtered_vms(
        provider=provider,
        region=region,
        max_price=max_price
    )
    write_csv(filename, rows)
    return filename


def export_cheapest_vm():
    ensure_export_dir()
    filename = f"{EXPORT_DIR}/cheapest_vm_{timestamp()}.txt"
    vm = get_cheapest_vm()

    with open(filename, "w") as f:
        f.write("Cheapest VM Across All Providers\n")
        f.write("=" * 40 + "\n")
        f.write(f"Provider : {vm[0]}\n")
        f.write(f"Instance : {vm[1]}\n")
        f.write(f"vCPU     : {vm[2]}\n")
        f.write(f"Memory   : {vm[3]} GB\n")
        f.write(f"Price    : ${vm[4]}/hour\n")
        f.write(f"Region   : {vm[5]}\n")

    return filename


def write_csv(filename, rows):
    headers = [
        "Provider",
        "Instance",
        "vCPU",
        "Memory(GB)",
        "Price($/hr)",
        "Region"
    ]
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
