# Python Command-Line Slot Machine

A text-based, interactive 3x3 slot machine game built using Python. This project simulates a real slot machine game cycle where users can deposit virtual currency, select the number of betting lines, specify their bet per line, and spin the slot machine to track their wins or losses.

## Features

- **Interactive Betting System:** Allows players to simulate depositing funds, managing a dynamic balance, and calculating individual per-line stakes.
- **Dynamic Line Selection:** Players can choose to bet on 1 to 3 horizontal lines simultaneously.
- **RNG-Driven Reel System:** Uses python's `random` module to simulate independent matrix column generations based on customizable symbol weights.
- **Automated Payout Engine:** Scans across selected lines to identify winning combinations and accurately credit multi-tiered rewards back to the player's balance.
- **Input Validation:** Prevents bad input or structural crashes by cleaning and validating all numeric terminal choices (deposits, lines, and bets).

---

## Game Rules & Payout Structure

The slot machine generates a **3x3 grid** of symbols (`A`, `B`, `C`, `D`). To win on a selected line, all three symbols on that horizontal line must match. 

### Rarity and Multipliers
Symbols have inversely proportional probabilities and multipliers (rarer symbols yield higher rewards):

| Symbol | Total in Pool (Frequency) | Multiplier Value |
| :----: | :-----------------------: | :--------------: |
|   **A** | 2 (Rarest)                | 5x               |
|   **B** | 3                         | 4x               |
|   **C** | 4                         | 3x               |
|   **D** | 5 (Most Common)           | 2x               |

*Example Formula: `Line Winnings = Symbol Value Multiplier * Bet Per Line`*

---

## Getting Started

### Prerequisites
- Python 3.6 or higher installed on your machine. No external third-party libraries are required.

### Installation
1. Clone this repository or download the source script file:
   ```bash
   git clone [https://github.com/your-username/python-slot-machine.git](https://github.com/your-username/python-slot-machine.git)
   cd python-slot-machine