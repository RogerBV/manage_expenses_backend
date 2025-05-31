import pytest

from src.dao.category_dao import CategoryDAO
from src.models.new_category_model import NewCategoryModel

@pytest.mark.asyncio
async def test_insert_category():
    category_name = "CATEGORY 1000"
    
    category_dao = CategoryDAO()
    result = await category_dao.create_category(NewCategoryModel(name=category_name))
    category_id = result.id
    
    category_founded = await category_dao.get_category_by_id(category_id)
    
    assert category_founded.id > 0