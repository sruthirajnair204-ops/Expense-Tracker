# Console-Based Expense Tracker (Python Mini-Project)

A lightweight, interactive command-line application built entirely using pure Python. This project was developed as a college mini-project to demonstrate a solid understanding of fundamental programming concepts, control flow patterns, and real-time input validation without relying on external libraries or databases.

## Key Features

- **1. Add New Expense**: Allows logging an expense with dual-layer safety validation. Category names are strictly filtered to accept only alphabetical letters, and prices require clear numerical values.
- **2. View Expense**: Formats and prints a clean, indexed breakdown of all your tracked costs side-by-side with the Indian Rupee (`₹`) text symbol.
- **3. View Total Spent**: Uses built-in computational processing to calculate and output the exact aggregate sum of every recorded expenditure up to two decimal places.
- **4. Delete an Expense**: Features dynamic target deletion where entering an index serial number drops data elements cleanly out of system memory using standard synchronized list operations.
- **5. Exit Program**: Securely breaks out of the execution workspace thread and terminates the runtime session with a friendly closing notification.

## Python Core Concepts Covered

- **Dynamic Memory Collection**: Managing operational attributes together in real-time across synchronized parallel arrays (`categories=[]` and `amounts=[]`).
- **Data Mutation Methods**: Adding new list indexes dynamically via `.append()` and pulling elements back out accurately using index target extraction via `.pop()`.
- **Exception/Error Handling**: Building bulletproof execution frameworks using robust `try-except ValueError` blocks to catch and filter problematic strings or empty arguments.
- **System Synchronization**: Iterating smoothly across multiple storage variables simultaneously using standard positional mapping (`range(len())`).

## How to Run and Interact

1. Ensure you have **Python 3.x** installed locally.
2. Save the script on your system workspace as `main.py`.
3. Open a system Terminal window or use your IDE terminal runner (such as PyCharm) and input:
   ```bash
   python main.py
   ```
4. Enter integers **1 through 5** inside the text prompt line to control the utility interface directly.
