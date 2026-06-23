# ATM Management System (Python OOP)

## Overview
This project is a simple ATM Management System built using Python and Object-Oriented Programming (OOP).

The program allows users to:
- Create a PIN
- Change PIN
- Check Account Balance
- Withdraw Money

The ATM menu is displayed continuously until the user chooses to exit.

## Features

### 1. Create PIN
- Creates a new ATM PIN.
- Stores the initial account balance.

### 2. Change PIN
- Verifies the old PIN.
- Allows the user to set a new PIN.

### 3. Check Balance
- Verifies the PIN.
- Displays the current account balance.

### 4. Withdraw Money
- Verifies the PIN.
- Deducts the entered amount from the balance.
- Prevents withdrawal if balance is insufficient.

## Concepts Used
- Classes and Objects
- Constructor (`__init__`)
- Instance Variables
- Methods
- Conditional Statements (`if-elif-else`)
- User Input (`input()`)
- Basic Banking Logic

## Class Structure

### Class: `Atm`

#### Attributes
- `pin` : Stores user's ATM PIN.
- `balance` : Stores account balance.

#### Methods
- `menu()` : Displays ATM options.
- `create_pin()` : Creates a new PIN and balance.
- `change_pin()` : Changes existing PIN.
- `check_balance()` : Shows account balance.
- `withdraw()` : Withdraws money from account.

## How to Run

1. Save the file as `ObjectandClass.py`
2. Open Terminal or Command Prompt.
3. Navigate to the file location.
4. Run:

```bash
python ObjectandClass.py
