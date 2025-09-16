def convert(amount, rates):

    rupee = amount * rates['R']
    pound = amount * rates['P']
    yen = amount * rates['Y']

    return rupee, pound, yen

def main():

    conversion = {'R': 83.50, 'P': 0.77, 'Y': 7.20}

    while(True):

        num = (input("\nEnter dollar ($)(* to exit): "))

        if num == '*':

            print("Bye")
            break;
        
        cut = num.split('@')
        dollars =[]

        for x in cut:

            if x.replace('.', '', 1).isdigit():

                dollars.append(float(x))

            else:

                print(f"Ignoring invalid entry: {x}")

        if not dollars:

            print("No valid dollar amounts entered.")
            continue
            
        print("\nDollar ($)    Indian Rupee (R)    British Pound (Pound)    Chinese Yuan (Y)")

        for y in dollars:
            rupee, pound, yen = convert(y, conversion)
            print(f"{y:<14.2f}{rupee:<22.2f}{pound:<22.2f}{yen:<.2f}")

main()