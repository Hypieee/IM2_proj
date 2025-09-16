def convert_dollar(amount, rates):

    rupee = amount * rates['R']
    pound = amount * rates['P']
    yen = amount * rates['Y']
    return rupee, pound, yen


def main():
    conversion_rates = {
        'R': 83.50,   # 1 USD = 83.50 Indian Rupee
        'P': 0.77,    # 1 USD = 0.77 British Pound
        'Y': 7.20     # 1 USD = 7.20 Chinese Yuan
    }

    while True:
        user_input = input("\nEnter dollar ($) (* to exit): ").strip()
        if user_input == '*':
            print("Bye")
            break

        parts = user_input.split('@')
        dollars = []

        for p in parts:
            if p.replace('.', '', 1).isdigit():
                dollars.append(float(p))
            else:
                print(f"Ignoring invalid entry: {p}")

        if not dollars:
            print("No valid dollar amounts entered.")
            continue

        print("\nDollar ($)    Indian Rupee (₹)    British Pound (£)    Chinese Yuan (¥)")
        for d in dollars:
            rupee, pound, yen = convert_dollar(d, conversion_rates)
            print(f"{d:<14.2f}{rupee:<22.2f}{pound:<22.2f}{yen:<.2f}")

main()
