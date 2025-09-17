shop = {}

shop["0"] = "underwear"
shop["1"] = "tank top"
shop["2"] = "jacket"

for y in shop.values():
    print(f"Shopping item: {y}")

print(f"\nYou have {len(shop)} items in the cart")

while True:
    action = input("\nWhat would you like to do [A]dd [C]hange [R]emove [D]isplay [S]earch ? ")

    match action.upper():
        case 'A':
            choice = input("Enter an item to add: ")
            new_key = action(len(shop))   # create next key
            shop[new_key] = choice
            print(f"{choice} added with key {new_key}")

        case 'C':
            choice = input("\nEnter a key to change: ")

            if choice in shop:
                print(f"Found {shop[choice]} item")
                new_value = input("\nEnter new value: ")
                shop[choice] = new_value
                print("\nUpdated Cart:")
                for x, y in shop.items():
                    print(x, y)
            else:
                print("I'm sorry, not in the cart")

        case 'R':
            choice = input("Enter a key to remove: ")

            if choice in shop:
                removed_value = shop.pop(choice)
                print(f"The key {choice} with value {removed_value} has been deleted\n")
                for x, y in shop.items():
                    print(x, y)
            else:
                print("Key not found")

        case 'D':
            print("\nDisplaying Values")
            print("\nKey      Value")
            for x, y in shop.items():
                print(x, "\t", y)

        case 'S':
            choice = input("Enter a key/item to search: ")

            if choice in shop:  # search by key
                print(f"Found key {choice} with item: {shop[choice]}")
            else:  # search by value
                found = False
                for k, v in shop.items():
                    if v.lower() == choice.lower():
                        print(f"Found item: {v} (key: {k})")
                        found = True
                        break
                if not found:
                    print("I'm sorry, not in the cart")
