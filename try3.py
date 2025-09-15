myList = []
myList = ["ash", "russ", "thom", "paul"];

print(myList[2])
print(myList[::-1])
print(myList[1:3:2])
print(myList)

myList.append("mar")
lista = ["john", "kurt", "prince", "jan" ]
myList.append(lista)
myList.insert(1, "prin")
myList.pop(0)

list2= ["Monje", "Espiritu"]
print (myList + list2)

# print(myList.sort())

myList.reverse()
print(myList)

myList2 = []

for x in range (3):
    print("Enter a number: ")
    num=float(input())
    myList2.append(num)
print(myList2)

nestedList = [[12, 5, 3], [6, 9, 5]]
nestedList[1][0]
nestedList[0][1]

for x in range (len(nestedList)):
    for y in range(len(nestedList[x])):
        print(f"{nestedList[x][y]}", end=" ")
    print()

# for x in myList:
#     print(f"{x}", end=" ")
    
# for y in range(len(myList)):
#     print(f"{myList[y]}", end=" ")