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



