from fastapi import APIRouter, Depends
from src.models.registered_category_model import RegisteredCategoryModel
from src.models.new_category_model import NewCategoryModel
from src.dao.category_dao import CategoryDAO
from src.dao.dependencies import get_db
from sqlalchemy.orm import Session

category_router = APIRouter(
    prefix='/Category',
    tags=['Category']
)

@category_router.get('')
async def get_categories(db: Session = Depends(get_db)) -> list[RegisteredCategoryModel]:
    category_dao = CategoryDAO(db)
    return await category_dao.get_categories()


@category_router.put('')
async def create_category(new_category_model: NewCategoryModel, db: Session = Depends(get_db)) -> RegisteredCategoryModel:
    category_dao = CategoryDAO(db)
    return await category_dao.create_category(new_category_model)