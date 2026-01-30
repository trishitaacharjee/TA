import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tabulate import tabulate
from src.cost_analyzer import (
    get_all_vms,
    get_filtered_vms,
    get_cheapest_vm
)
from src.report_generator import (
    export_all_vms,
    export_filtered_vms,
    export_cheapest_vm
)


def show_table(rows):
    headers = ["Provider", "Instance", "vCPU", "Memory", "Price/Hr", "Region"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))


def menu():
    print("\n" + "=" * 40)
    print(" CLOUD COSTSENSE MENU ")
    print("=" * 40)
    print("1. Show all VM pricing")
    print("2. Show cheapest VM")
    print("3. Filter VM options")
    print("4. Generate report")
    print("5. Exit")
    print("=" * 40)


def main():
    while True:
        menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\nALL VM PRICING\n")
            show_table(get_all_vms())

        elif choice == "2":
            print("\nCHEAPEST VM\n")
            show_table([get_cheapest_vm()])

        elif choice == "3":
            print("\nFILTER VMs\n")
            provider = input("Provider (AWS/Azure/GCP or blank): ").strip() or None
            region = input("Region (or blank): ").strip() or None
            max_price = input("Max price/hr (or blank): ").strip()

            max_price = float(max_price) if max_price else None

            results = get_filtered_vms(
                provider=provider,
                region=region,
                max_price=max_price
            )

            if results:
                show_table(results)
            else:
                print("No matching results found.")

        elif choice == "4":
            print("\nREPORT OPTIONS")
            print("1. Full VM pricing report (CSV)")
            print("2. Filtered VM report (CSV)")
            print("3. Cheapest VM report (TXT)")

            rchoice = input("Choose (1-3): ").strip()

            if rchoice == "1":
                file = export_all_vms()
                print(f"Report generated: {file}")

            elif rchoice == "2":
                provider = input("Provider (optional): ").strip() or None
                region = input("Region (optional): ").strip() or None
                max_price = input("Max price/hr (optional): ").strip()
                max_price = float(max_price) if max_price else None

                file = export_filtered_vms(
                    provider=provider,
                    region=region,
                    max_price=max_price
                )
                print(f"Report generated: {file}")

            elif rchoice == "3":
                file = export_cheapest_vm()
                print(f"Report generated: {file}")

            else:
                print("Invalid report choice.")

        elif choice == "5":
            print("Exiting Cloud CostSense. Bye 👋")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
