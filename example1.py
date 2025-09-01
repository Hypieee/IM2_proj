size = int (input("Enter Size: "))

for x in range (1, size+1): 
    for y in range(1, size+1):
        if x%2==0:
            print(f"*", end=" ")
        else:
            print(f"o", end=" ")
    print()