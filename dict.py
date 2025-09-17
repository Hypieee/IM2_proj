shop = {}

shop["0"] = "underwear"
shop["1"] = "tank top"
shop["2"] = "jacket"

for y in shop.values():
    print(f"Shopping items: ", y)

print(f"\nYou have {len(shop)} items in the cart")

while(True):

    action = input("\nWhat would you like to do [A]dd [C]hange items [R]emove [D]isplay [S]earch ?")

    match action:
        case 'A':
            choice = input("Enter an item to add: ")
            new_key = str(len(shop))
            shop[new_key] = choice
            print(f"{choice} added with key {new_key}")

        case 'C':
            choice = input("\nEnter a key to change: ")

            if choice in shop:
                print(f"Found {shop[choice]} item")
                new_value = input("\nEnter value: ")
                shop[choice] = new_value
                print()
                for x,y in shop.items():
                    print(x, y, end = " \n")
            else:
                print("Im sorry, not in the cart")

        case 'R':
            choice = input("Enter a key to remove: ")

            if choice in shop:
                removed_value = shop.pop(choice)

                print(f"The key {choice} with value {removed_value} has been deleted\n")

                for x,y in shop.items():
                    print(x, y, end = " \n")
            else:
                print("Key not found")
        
        case 'D':
            print("\nDisplaying Values")
            print("\nKey      Value")
            for x, y in shop.items():
                print(x,"\t", y, end = " \n")
            print()
        
        case 'S':
            choice = input("Enter a key/item to search: ")

            if choice.isdigit():
                key = int(choice)
                value = shop.get(choice)
                if value:
                    print(f"Found key {key} with item: {value}")
                else:
                    print("Im sorry, not in the cart")
            else:
                found = False
                for k, v in shop.items():
                    if v.lower() == choice.lower():
                        print(f"Found {v} item")
                        found = True
                        break
                if not found:
                    print("Im sorry, not in the cart")