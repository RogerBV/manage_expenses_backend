from .common.base import Base
from .common.base_entity import BaseEntity
from sqlalchemy import Column, String

class Category(Base, BaseEntity):
    __tablename__= "Category"
    name = Column(String(50), nullable=False)