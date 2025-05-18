from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.dao.dependencies import get_db
from src.dao.expense_dao import ExpenseDAO
from src.models.registered_expense_model import RegisteredExpenseModel
from src.models.new_expense_model import NewExpenseModel

expense_router = APIRouter(
    prefix='/Expenses',
    tags=['Expenses']
)

@expense_router.get('')
async def get_expenses(db: Session = Depends(get_db)) -> list[RegisteredExpenseModel] :
    expenseDAO = ExpenseDAO(db)
    return await expenseDAO.get_expenses()

@expense_router.put('')
async def create_expense(newExpenseModel: NewExpenseModel, db: Session = Depends(get_db)) -> RegisteredExpenseModel:
    expenseDAO = ExpenseDAO(db)
    return await expenseDAO.create_expense(newExpenseModel)