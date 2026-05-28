# Console-Based Expense Tracker

A lightweight, terminal-based Expense Tracker application built entirely using pure Python. This project was developed as a college mini-project to demonstrate foundational programming logic, control flow structures, and dynamic data management without relying on external libraries or graphical interfaces.

## Features

- **Add New Expenses (Option 1)**: Input daily expenses with strict data validation. Category names must contain only alphabetical characters, and amounts must be numerical.
- **View Recorded Expenses (Option 2)**: Displays an organized, cleanly indexed checklist tracking every logged expense alongside the Indian Rupee (₹) symbol.
- **Calculate Total Spend (Option 3)**: Instantly sums up all expenditures currently stored in the system memory.
- **Delete Specific Entries (Option 4)**: Allows removing mistaken entries smoothly by entering their corresponding list item number. Both parallel tracking lists are immediately updated and synchronized.
- **Graceful Program Exit (Option 5)**: Ends the interactive environment cleanly with a closing user message.

## Python Core Concepts Covered

- **Dynamic Data Structures**: Dual parallel lists (`categories` and `amounts`) managed simultaneously using `.append()` and `.pop()`.
- **Control Loops & Flow**: Continuous application runtime via a `while True` loop alongside conditional `if-elif-else` routing.
- **Data Validation & Robustness**: Bulletproof `try-except` blocks preventing runtime crashes from bad data conversions (handling strings inside integer or floating-point parameters).
- **List Indexing**: Leveraging `range(len())` to bind and pair separate multi-list structural values cleanly inside user-facing terminal logs.

## How to Run the Application

1. Ensure you have **Python 3.x** installed on your machine.
2. Copy the code into a local script file named `main.py` or `expense_tracker.py`.
3. Open your terminal or IDE console (e.g., PyCharm) and execute the program:
   ```bash
   python main.py
   ```
4. Interact directly with the system by choosing options `1` through `5` inside the terminal window prompt.
