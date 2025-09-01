firsNum = int (input(" enter first num: "))
secNum = int (input ("enter second num: "))

op = input("select operator: 1, 2, 3, 4")

if op == 1:
    print(f"result {firsNum + secNum}")
elif op == 2:
   print(f"result {firsNum - secNum}")
elif op == 3:
   print(f"result {firsNum * secNum}")
elif op == 4:
   print(f"result {firsNum / secNum}")
