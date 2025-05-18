from pydantic import BaseModel
from datetime import date

class RegisteredExpenseModel(BaseModel):
    id: int
    name: str
    price: float
    expenseDate: date
    categoryId: int
    categoryName: str