# nlist = []
# row = int (input("Row: "))
# col = int (input("Col: "))
# sum = 0
# ave = 0

# for x in range(row):
#     print(f"Row{x+1}")
#     list1=[]

#     for y in range(col):
#         print("Enter row score: ")
#         num2=int(input())
#         list1.append(num2)
#     nlist.append(list1)

# for x in nlist:
#     for y in x:
#         print(f"{y}", end=" ")
#         sum+=y
#     print()

# for x in list1:
#     for y in x:
#         sum += y 
#         ave = sum / len(nlist)
# print(f"Sum: {sum}")
# print(f"Average: {ave}")

# myTuple=(1,4,5,6)
# x=list(myTuple)
# x.append(8)
# x.append(70)
# x.remove(5)
# x.pop()

# myTuple2 = tuple(x)
# print(myTuple2)

# for x in myTuple2:
#     print(x, end=" ")

myDIct = {"id" : "URDA-011", "name" : "Velasco", "Salary" : "10000.00"}
myDIct["age"] = 28
myDIct["sex"] = "Male"
myDIct["name"] = "Tugare"
myDIct.popitem()
myDIct.pop("name")

for x in myDIct.keys():
    print(x)
for y in myDIct.values():
    print(y)
for x,y in myDIct.items():
    print(f"Key: {x}, Value: {y}", end = " ")
