MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
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

def get_bet(): #this is to ask user that though you have deposited a certain amount, how much do you want to bet out..
    while True:
        betamount = input("Enter the bet amount from " + str(MIN_BET) + " to " + str(MAX_BET)+ " for each line ")
        if betamount.isdigit():
            betamount = int(betamount)
            if MIN_BET <= betamount <= MAX_BET:
                break
            else:
                print("enter the amount in the mentioned range")
        else:
            print("enter a valid number")
    return betamount


def main():
    balance = deposit()
    lines = get_num_of_lines()
    betamount = get_bet()
    print(f"you are betting rupees {betamount} on {lines} lines, total bet is equal to: rupees {lines*betamount}")

main()
