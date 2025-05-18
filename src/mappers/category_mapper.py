from src.models.new_category_model import NewCategoryModel
from src.models.registered_category_model import RegisteredCategoryModel
from src.entities.category import Category

def to_category_entity(newCategoryModel: NewCategoryModel) -> Category:
    return Category(
        name = newCategoryModel.name
    )
    
def to_registered_category_model(categoryEntity: Category) -> RegisteredCategoryModel:
    return RegisteredCategoryModel(
        id = categoryEntity.id,
        name=categoryEntity.name
    )