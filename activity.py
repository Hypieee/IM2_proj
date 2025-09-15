
# for x in range (1):
#     for y in range(1, 101):
#         if y%10==0:
#             print(f"{y}*\n")
#         else:
#             value = x % y
#             if value==0:
#                 print(f"[{y}]\t", end=" ")
#             else:
#                 print(f"{y}*\t", end=" ")
#     print()

# while(True):

#     str = input("Enter a String: ")

#     if str == "*":
#         break;
#     else:
#         print(f"Original String ")
#         print(str)
#         print(f"Reversed String ")
#         pal=str.lower()
#         rev=pal[::-1]
#         print(rev)
        
#         print(f"Palindrome?")
#         if rev == pal :
#             print("yes")
#         else:
#             print("no")

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

print(myList.sort())

myList.reverse()
print(myList)

for x in myList:
    print(f"{x}", end=" ")
    
# for y in range(len(myList)):
#     print(f"{myList[y]}", end=" ")
