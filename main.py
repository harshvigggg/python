MAX_LINES = 3

def deposit():
    while True:
        amount = input("enter the amount you want to deposit:")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break;
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    return amount

def get_num_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("enter valid number of lines")
        else:
            print("enter a number")
    return lines

def main():
    balance = deposit()
    lines = get_num_of_lines()
    print(balance, lines)

main()