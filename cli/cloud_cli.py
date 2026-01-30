import os
import sys
import argparse
from tabulate import tabulate

# 🔧 Fix import path (VERY IMPORTANT)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from src.cost_analyzer import (
    get_all_vms,
    get_filtered_vms,
    get_cheapest_vm
)


HEADERS = ["Provider", "Instance", "vCPU", "Memory (GB)", "Price ($/hr)", "Region"]


def show_table(rows):
    if not rows:
        print("No results found.")
        return

    # rows are tuples → tabulate needs list of lists
    table_data = [list(row) for row in rows]
    print(tabulate(table_data, headers=HEADERS, tablefmt="grid"))


def main():
    parser = argparse.ArgumentParser(description="Cloud CostSense CLI")

    subparsers = parser.add_subparsers(dest="command")

    # all
    subparsers.add_parser("all", help="Show all VM pricing")

    # cheapest
    subparsers.add_parser("cheapest", help="Show cheapest VM")

    # filter
    filter_parser = subparsers.add_parser("filter", help="Filter VM options")
    filter_parser.add_argument("--provider", type=str)
    filter_parser.add_argument("--min-vcpu", type=int)
    filter_parser.add_argument("--min-memory", type=float)
    filter_parser.add_argument("--max-price", type=float)
    filter_parser.add_argument("--region", type=str)

    args = parser.parse_args()

    if args.command == "all":
        print("\nAll VM Pricing:\n")
        show_table(get_all_vms())

    elif args.command == "cheapest":
        print("\nCheapest VM:\n")
        result = get_cheapest_vm()
        show_table([result] if result else [])

    elif args.command == "filter":
        print("\nFiltered Results:\n")
        results = get_filtered_vms(
            provider=args.provider,
            min_vcpu=args.min_vcpu,
            min_memory=args.min_memory,
            max_price=args.max_price,
            region=args.region
        )
        show_table(results)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
