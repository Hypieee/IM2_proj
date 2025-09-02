while (True):
    rows = int(input("Enter row: "))
    cols = int(input("Enter col: "))

    if rows <= 0 or cols <= 0:
        break;

    search_val = int(input("Search: "))

    found = False
    print()
    for x in range(1, rows + 1):
        for y in range(1, cols + 1):
            value = x * y
            if value == search_val:
                print(f"[{value}]", end=" ")
                found = True
            else:
                print(value, end=" ")
        print()

    if not found:
        print(f"\n{search_val} not found.")
    else:
        print(f"\n{search_val} found in the table.")
