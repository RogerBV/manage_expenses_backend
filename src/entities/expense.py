from .common.base import Base
from .common.base_entity import BaseEntity
from sqlalchemy import Column, String, DECIMAL, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from .category import Category

class Expense(Base, BaseEntity):
    __tablename__='Expense'
    name = Column(String(50), nullable=False)
    price = Column(DECIMAL, nullable=False)
    expenseDate = Column(Date, nullable=False)
    categoryId = Column(Integer, ForeignKey('Category.id'), nullable=False)
    category = relationship('Category', backref='expenses', lazy = 'joined')