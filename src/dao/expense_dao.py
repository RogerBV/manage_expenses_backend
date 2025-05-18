from src.entities.expense import Expense
from src.models.registered_expense_model import RegisteredExpenseModel
from src.models.new_expense_model import NewExpenseModel
from sqlalchemy.orm import Session
from src.mappers.expense_mapper import to_registered_expense_model, to_expense_entity

class ExpenseDAO():
    def __init__(self, db: Session):
        self.db = db
    
    async def get_expenses(self) -> list[RegisteredExpenseModel]:
        expenses = self.db.query(Expense).all()
        return [to_registered_expense_model(obj) for obj in expenses]
    
    async def create_expense(self, new_expense_model: NewExpenseModel) -> RegisteredExpenseModel:
        new_expense_entity = to_expense_entity(new_expense_model)
        self.db.add(new_expense_entity)
        self.db.commit()
        self.db.refresh(new_expense_entity)
        return to_registered_expense_model(new_expense_entity)
    
    async def get_expense_by_id(self, expense_id: int) -> RegisteredExpenseModel:
        expense = self.db.query(Expense).filter(Expense.id == expense_id).first()
        return to_registered_expense_model(expense) if expense else None