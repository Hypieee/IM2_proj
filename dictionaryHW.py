def display_items(mydict):
    print("\nDisplaying Values")
    print("Key      Value")
    for x, y in mydict.items():
        print(x,"\t", y, end = " \n")
    print()

def search_items(mydict):
    choice = input("\nEnter item to search (by value or key): ")
    
    # check if input is digit (search by key)
    if choice.isdigit():
        key = int(choice)
        value = mydict.get(key)
        if value:
            print(f"Found key {key} with item: {value}")
        else:
            print("Im sorry, not in the cart")
    else:
        print("Im sorry, not in the cart")

def remove_items(mydict):
    choice = input("\nEnter key to remove: ")
    if choice.isdigit():
        key = int(choice)
        if key in mydict:
            removed_value = mydict.pop(key)
            print(f"The key {key} with value {removed_value} has been deleted\n")
            for x,y in mydict.items():
                print(x, y, end = " \n")
        else:
            print("Key not found")
    else:
        print("Key not found")

def change_items(mydict):
    choice = input("\nEnter key to search: ")
    if choice.isdigit():
        key = int(choice)
        if key in mydict:
            print(f"Found {mydict[key]} item")
            new_value = input("Enter value: ")
            mydict[key] = new_value
            print()
            for x,y in mydict.items():
                print(x, y, end = " \n")
        else:
            print("Im sorry, not in the cart")
    else:
        print("Im sorry, not in the cart")


def main():
    mydict = {
        0: "underwear",
        1: "tank top",
        2: "jacket"
    }

    print(f"\nYou have {len(mydict)} items in the cart")

    while True:
        action = input(
            "\nWhat would you like to do "
            "[C]hange items [R]emove [D]isplay S[earch] ? "
        ).strip().lower()

        if action == 'd':
            display_items(mydict)
        elif action == 's':
            search_items(mydict)
        elif action == 'r':
            remove_items(mydict)
        elif action == 'c':
            change_items(mydict)
        else:
            print("Bye")
            break

main()
