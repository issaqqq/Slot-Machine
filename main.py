import random 

MAX_LINES = 3
MAX_BET = 1000
MIN_Bet = 1

ROWS = 3
COLS = 3

SymbolCount = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 5
}

SymbolValue = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def CheckWinnings(columns, lines, bets, values):
    winnings = 0
    winningLines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            SymbolCheck = column[line]
            if symbol != SymbolCheck:
                break
        else:
            winnings += values[symbol] * bets
            winningLines.append(line + 1)

    return winnings, winningLines
    
def GetSlotMachineSpin(rows, cols, symbols):
    allSymbols = []
    for symbol, SymbolCount in symbols.items():
        for _ in range(SymbolCount):
            allSymbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        currentSymbols = allSymbols[:]
        for _ in range(rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def PrintSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def GetDeposit():
    while True:
        amount = input("What amount would you like to deposit? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"You have successfully deposited ${amount} ")
                break
            else:
                print("Please enter a positive amount.")
        else:
            print("Invalid input. Please enter a numeric value.")
    return amount 

def GetNumberOfLines():
    while True:
        lines = input("Enter the number of Lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                print(f"You have entered {lines} lines")
                break
            else:
                print("Enter a valid number of lines. ")

        else:
            print("Enter a number. ")

    return lines
            
def GetBet():
    while True:
        bet = input("What would you like to bet on each line? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_Bet <= bet <= MAX_BET:
                print(f"You are betting ${bet} on each line")
                break
            else:
                print(f"Amount must be between ${MIN_Bet} - ${MAX_BET}. ")

        else:
            print("Enter a number. ")

    return bet

def main():
 balance = GetDeposit() 
 lines = GetNumberOfLines()
 while True:
    bet = GetBet()
    totalBet = bet * lines

    if totalBet > balance:
        print(f"You do not have enough amount, your current balance is ${balance}")
    else:
        break
      
 print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${totalBet}")
 slots = GetSlotMachineSpin(ROWS, COLS, SymbolCount)
 PrintSlotMachine(slots)
 winnings, winninglines = CheckWinnings(slots, lines, bet, SymbolValue)
 print(f"You won {winnings}")
 print(f"you won on lines: ", *winninglines)


main() 