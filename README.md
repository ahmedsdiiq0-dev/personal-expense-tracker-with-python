# Personal Expense Tracker 

My first Python project dedicated to managing and tracking personal daily expenses.

## 📖 Description
This is a Command-Line Interface (CLI) application designed to help users record and monitor their spending habits. The project is built using **Object-Oriented Programming (OOP)** principles with comprehensive type hints and robust error handling to ensure a smooth user experience.

## ✨ Features
- **Object-Oriented Design:** Modular classes (`Expense` and `ExpenseTracker`) for efficient expense management.
- **Type Hints:** Full type annotations for improved code clarity and maintainability.
- **Input Validation:** Robust `get_validated_input()` function with try-except blocks for error handling and data integrity.
- **Flexible Input Handling:** Users can press 'q' at any time to exit the input loop.
- **Categorization:** Organize expenses by categories (e.g., Food, Transport, Study) with case-insensitive matching.
- **Category-Based Totals:** Calculate total spending per category with the `get_category_total()` method.
- **Automated Summary:** Displays a formatted summary showing:
  - Total expenditure
  - Individual expense details (name, price, category)
  - Empty state handling when no expenses are recorded
- **Data Validation:** Ensures prices are greater than 0 before adding expenses.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Paradigm:** Object-Oriented Programming (OOP)
- **Development Environment:** Linux (Ubuntu)
- **Version Control:** Git & GitHub

## 🚀 How to Run

1. **Clone the repository:**
```bash
git clone https://github.com/ahmedsdiiq0-dev/personal-expense-tracker-with-python.git
```

2. **Navigate to the project directory:**
```bash
cd personal-expense-tracker-with-python
```

3. **Run the script:**
```bash
python3 expense-tracker.py
```

## 📝 Usage Example

```
Welcome to the Personal Expense Tracker!
--------------------------------------------------

Adding a new expense (type 'q' to finish):
Item name: Coffee
Item price: 5.50
Category: Food
✓ Expense added!

Adding a new expense (type 'q' to finish):
Item name: Bus Ticket
Item price: 2.00
Category: Transport
✓ Expense added!

Adding a new expense (type 'q' to finish):
q

--------------------------------------------------
Total Expenses: $7.50
--------------------------------------------------
Item: Coffee | Price: $5.50 | Category: Food
Item: Bus Ticket | Price: $2.00 | Category: Transport
--------------------------------------------------
```

## 📚 Class Structure

### `Expense`
Represents a single expense item with:
- `name`: Item name
- `price`: Cost of the item
- `category`: Expense category

### `ExpenseTracker`
Manages a collection of expenses with methods:
- `add_expense()`: Add a new expense
- `get_total()`: Calculate total expenses
- `get_category_total()`: Get total for a specific category
- `display_summary()`: Display formatted expense summary

## 🔧 Functions

- **`get_validated_input()`**: Handles user input with type conversion and validation
  - Parameters: `prompt`, `input_type`, `allow_quit`
  - Returns: Converted value or `None` if user quits

**Thank you :)**
