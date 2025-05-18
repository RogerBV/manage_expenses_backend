from sqlalchemy.orm import Session
from .sql_alchemy_models import Category
from src.models.registered_category_model import RegisteredCategoryModel
from src.models.new_category_model import NewCategoryModel
from src.mappers.category_mapper import to_registered_category_model, to_category_entity

class CategoryDAO():
    def __init__(self, db: Session):
        self.db = db
    
    async def get_categories(self) -> list[RegisteredCategoryModel]:
        categories = self.db.query(Category).all()
        return [to_registered_category_model(obj) for obj in categories]
    
    async def create_category(self, new_category_model: NewCategoryModel) -> RegisteredCategoryModel:
        new_category_entity = to_category_entity(new_category_model)
        self.db.add(new_category_entity)
        self.db.commit()
        self.db.refresh(new_category_entity)
        return to_registered_category_model(new_category_entity)
    
    async def get_category_by_id(self, category_id: int) -> RegisteredCategoryModel:
        category = self.db.query(Category).filter(Category.id == category_id).first()
        return to_registered_category_model(category) if category else None