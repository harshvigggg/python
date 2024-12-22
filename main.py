import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
        "A":2,
        "B":4,
        "C":6,
        "D":8
        }

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")

        print()


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
    while((betamount*lines) > balance):
        print("bet amount exceeded the balance, try again!")
        betamount = get_bet()
    print(f"you are betting rupees {betamount} on {lines} lines, total bet is equal to: rupees {lines*betamount}")
    
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)


main()
