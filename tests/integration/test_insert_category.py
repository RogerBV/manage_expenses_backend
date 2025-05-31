import pytest

from src.dao.category_dao import CategoryDAO
from src.models.new_category_model import NewCategoryModel

async def test_insertCategory():
    categoryName = "CATEGORY 1000"
    
    categoryDAO = CategoryDAO()
    result = await categoryDAO.create_category(NewCategoryModel(name=categoryName))
    categoryId = result.id
    
    categoryFounded = await categoryDAO.get_category_by_id(categoryId)
    
    assert categoryFounded.id > 0