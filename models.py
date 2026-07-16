from sqlalchemy import Column, Integer, String, Float
from database import Base

class ExpenseDB(Base):
    __tablename__="expenses"

    id=Column(Integer, primary_key=True, index=True)
    category=Column(String)
    description=Column(String)
    amount=Column(Float)