from typing import Optional, List


class Expense:
    """Represents a single expense item."""
    
    def __init__(self, name: str, price: float, category: str) -> None:
        self.name = name
        self.price = price
        self.category = category
    
    def __str__(self) -> str:
        return f"Item: {self.name} | Price: ${self.price:.2f} | Category: {self.category}"


class ExpenseTracker:
    """Manages a collection of expenses."""
    
    def __init__(self) -> None:
        self.expenses: List[Expense] = []
    
    def add_expense(self, expense: Expense) -> None:
        """Add an expense to the tracker."""
        self.expenses.append(expense)
    
    def get_total(self) -> float:
        """Calculate total expenses."""
        return sum(expense.price for expense in self.expenses)
    
    def get_category_total(self, category: str) -> float:
        """Get total expenses for a specific category."""
        return sum(expense.price for expense in self.expenses if expense.category.lower() == category.lower())
    
    def display_summary(self) -> None:
        """Display summary of all expenses."""
        print("\n" + "-" * 50)
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print(f"Total Expenses: ${self.get_total():.2f}")
            print("-" * 50)
            for expense in self.expenses:
                print(expense)
        print("-" * 50)


def get_validated_input(prompt: str, input_type: type = str, allow_quit: bool = True) -> Optional[any]:
    """
    Get and validate user input.
    
    Args:
        prompt: The input prompt to display
        input_type: Type to convert input to (str, float, etc.)
        allow_quit: Whether 'q' exits the program
    
    Returns:
        Converted value or None if user quits
    """
    while True:
        value = input(prompt)
        
        if allow_quit and value.lower() == "q":
            return None
        
        if not value.strip():
            print("⚠ Input cannot be empty. Try again.")
            continue
        
        try:
            return input_type(value) if input_type != str else value.strip()
        except ValueError:
            print(f"⚠ Invalid input! Please enter a valid {input_type.__name__}.")


def main() -> None:
    """Main program flow."""
    print("-" * 50)
    print("Welcome to the Personal Expense Tracker!")
    print("-" * 50)
    
    tracker = ExpenseTracker()
    
    while True:
        print("\nAdding a new expense (type 'q' to finish):")
        
        name = get_validated_input("Item name: ")
        if name is None:
            break
        
        price = get_validated_input("Item price: ", float)
        if price is None:
            break
        
        category = get_validated_input("Category: ")
        if category is None:
            break
        
        if price <= 0:
            print("⚠ Price must be greater than 0.")
            continue
        
        expense = Expense(name, price, category)
        tracker.add_expense(expense)
        print("✓ Expense added!")
    
    tracker.display_summary()


if __name__ == "__main__":
    main()
