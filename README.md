# 🎰 Python Slot Machine Game

A simple command-line Slot Machine game built with Python. Players can deposit money, place bets on multiple lines, spin the slot machine, and win rewards based on matching symbols.

This project demonstrates Python fundamentals including functions, loops, dictionaries, lists, randomization, and user input validation.

---

## 📌 Features

- 💰 Deposit virtual money before playing
- 🎲 Bet on 1–3 winning lines
- 💵 Choose your bet amount per line
- 🎰 Randomly generated slot machine spins
- 🏆 Winning calculation based on matching symbols
- 📊 Live balance tracking
- ✅ Input validation for all user entries

---

## 🛠️ Built With

- Python 3
- `random` module

No external libraries are required.

---

## 📂 Project Structure

```
slot-machine/
│── main.py
│── README.md
```

---

## ▶️ How to Run

1. Clone this repository

```bash
git clone https://github.com/issaqqq/slot-machine.git
```

2. Navigate to the project directory

```bash
cd slot-machine
```

3. Run the program

```bash
python main.py
```

---

## 🎮 How to Play

1. Deposit an amount.
2. Choose the number of lines to bet on (1–3).
3. Enter your bet amount for each line.
4. Spin the slot machine.
5. If all symbols on a selected line match, you win according to the symbol value.
6. Your winnings are added to your balance, and the game continues until you quit.

---

## 💎 Symbol Values

| Symbol | Value |
|---------|------:|
| A | 5 |
| B | 4 |
| C | 3 |
| D | 2 |

---

## 🎲 Symbol Distribution

The probability of each symbol appearing is controlled using the following counts:

| Symbol | Count |
|---------|------:|
| A | 2 |
| B | 3 |
| C | 4 |
| D | 5 |

Symbols with higher counts appear more frequently.

---

## 📷 Example Gameplay

```
What amount would you like to deposit? 100

Current balance is $100

Enter the number of lines to bet on (1-3): 2

What would you like to bet on each line? 10

You are betting $10 on 2 lines.
Total bet is equal to $20

A | B | A
C | C | C
D | A | B

You won 30
You won on lines: 2

Current balance is $110
```

---

## 🧠 Concepts Used

- Functions
- Dictionaries
- Lists
- Nested loops
- Random module
- Input validation
- Conditional statements
- Balance management
- Game logic

---

## 🚀 Future Improvements

- Colored terminal output
- Multiple slot machine themes
- Jackpot system
- Bonus rounds
- Save/load player balance
- Graphical User Interface (Tkinter or Pygame)
- Sound effects and animations

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Made with ❤️ using Python.