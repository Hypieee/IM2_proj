while(True):
    num = int(input("Enter a Number: "))

    if num%5==0 and num%6 != 0:
        print("It is divisibke by 5")
    elif num%6==0 and num%5 != 0:
        print("It is dividible by 6")
    elif num%5==0 and num%6==0:
        print("it is divisible by 5 ad 6")
    else:
        print("it is not divisible by 5 or 6")