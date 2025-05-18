from src.models.registered_expense_model import RegisteredExpenseModel
from src.models.new_expense_model import NewExpenseModel
from src.entities.expense import Expense

def to_registered_expense_model(expense: Expense) -> RegisteredExpenseModel:
    return RegisteredExpenseModel(
        id=expense.id,
        name=expense.name,
        price=expense.price,
        expenseDate=expense.expenseDate,
        categoryId=expense.categoryId,
        categoryName=expense.category.name
    )
    
def to_expense_entity(newExpenseModel: NewExpenseModel) -> Expense:
    return Expense(
        name=newExpenseModel.name,
        price=newExpenseModel.price,
        expenseDate=newExpenseModel.expenseDate,
        categoryId=newExpenseModel.categoryId,
    )