from fastapi import FastAPI
from pydantic import BaseModel
from oop_expense_tracker import ExpenseTracker
from database import engine,SessionLocal
from models import Base,ExpenseDB


Base.metadata.create_all(bind=engine)
app = FastAPI()
tracker = ExpenseTracker()

@app.get("/")
def home():
    return {"message":"Hello Prince! Your first FastAPI app is running"}

@app.get("/greet/{name}")
def greet(name: str):
    return{"message":f"Hello {name},Welcome to FastAPI!"}


@app.get("/expenses")
def get_expenses():
    db = SessionLocal()
    view_expenses = db.query(ExpenseDB).all()
    db.close()
    return view_expenses

class Expense(BaseModel):
    category:str
    description:str
    amount:float
    

@app.post("/expenses")
def add_expense(expense: Expense):
    db=SessionLocal()
    new_expense = ExpenseDB(category=expense.category, description=expense.description, amount=expense.amount)
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    db.close()
    return{"message":"Expense added sucessfully!","data":expense}

@app.get("/expenses/total")
def total_expense():
    db=SessionLocal()
    total = db.query(ExpenseDB).all()
    total_amount = sum(expense.amount for expense in total)
    db.close()
    return {"total_expense": total_amount}

@app.delete("/expenses/{description}")
def delete_expense(description: str):
    db = SessionLocal()
    expense_to_delete = db.query(ExpenseDB).filter(ExpenseDB.description == description).first()
    if expense_to_delete:
        db.delete(expense_to_delete)
        db.commit()
        db.close()
        return {"message": f"Expense with description '{description}' deleted successfully."}
    else:
        db.close()
        return {"message": f"No expense found with description '{description}'."}
    

