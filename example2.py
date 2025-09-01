while(True):    
    str = input (print("enter string: "))

    if (str=="/"):
        break;
    for z in str:
        print(z)
    for a in range(len(str)):
        match str[a]:
            case "a":
                print(f"{str[a]} Vowel ")
            case "e":
                print(f"{str[a]} Vowel ")
            case "i":
                print(f"{str[a]} Vowel ")
            case "o":
                print(f"{str[a]} Vowel ")
            case "u":
                print(f"{str[a]} Vowel ")
            case _:
                print(f"{str[a]} Consonant ")