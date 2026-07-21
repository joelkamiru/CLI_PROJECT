from tabulate import tabulate

def print_table(data_rows, headers, title):
    """Utility function using the tabulate PyPI package to print clear tables."""
    print(f"\n=== {title} ===")
    if not data_rows:
        print("No records found.")
        return
    print(tabulate(data_rows, headers=headers, tablefmt="grid"))