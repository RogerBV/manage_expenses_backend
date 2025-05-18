from pydantic import BaseModel
from datetime import date

class NewExpenseModel(BaseModel):
    name: str
    price: float
    expenseDate: date
    categoryId: int