

def print_table(data_rows, headers, title):

    print(f"\n=== {title} ===")
    
    if not data_rows:
        print("No records found.")
        return
    for row in data_rows:
        print(row)