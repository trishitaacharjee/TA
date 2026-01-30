import argparse
from src.cost_analyzer import get_all_vms, get_filtered_vms, get_cheapest_vm

def print_table(rows):
    print("\nProvider | Instance | vCPU | Memory(GB) | Price($/hr) | Region")
    print("-" * 70)
    for p, it, v, mem, price, r in rows:
        print(f"{p} | {it} | {v} | {mem} | {price} | {r}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider")
    parser.add_argument("--min-vcpu", type=int)
    parser.add_argument("--min-memory", type=float)
    parser.add_argument("--max-price", type=float)
    parser.add_argument("--region")
    parser.add_argument("--cheapest", action="store_true")

    args = parser.parse_args()

    if args.cheapest:
        print("\nCheapest VM Across All Providers:\n")
        print_table([get_cheapest_vm()])
        return

    if any(vars(args).values()):
        rows = get_filtered_vms(
            args.provider, args.min_vcpu,
            args.min_memory, args.max_price, args.region
        )
        print("\nFiltered VM Results:\n")
        print_table(rows)
        return

    print("\nAll VM Pricing Options:\n")
    print_table(get_all_vms())

if __name__ == "__main__":
    main()
