class Expense:
    def __init__(self,category,description,amount):
        self.category = category
        self.description = description
        self.amount = amount


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self,category,description,amount):
        expense = Expense(category,description,amount)
        self.expenses.append(expense)
        return expense
    
    def view_expense(self):
        return self.expenses

    def total_expense(self):
        total_amount=0
        for expense in self.expenses:
            total_amount+=expense.amount
        return(f"Total Amount: ${total_amount}")
    
    def delete_expense(self,description):
        for expense in self.expenses:
            if expense.description == description:
                self.expenses.remove(expense)
                return (f"{description} deleted successfully.")
        return(f"No such expense {description} found!")


if __name__=="__main__":
    tracker = ExpenseTracker()

    tracker.add_expense("Food","Lunch at hotel",150)
    tracker.add_expense("Travel","Bus ticket",50)
    tracker.add_expense("Shopping","New shirt",500)

    print("\n--- All Expenses ---")
    tracker.view_expense()

    print("\n--- Total ---")
    tracker.total_expense()

    print("\n--- Deleting Lunch ---")
    tracker.delete_expense("Lunch at hotel")

    print("\n--- After Deletion ---")
    tracker.view_expense()



