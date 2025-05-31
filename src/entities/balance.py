from sqlalchemy import Column, Date, Integer, ForeignKey, DECIMAL
from .common.base import Base
from .common.base_entity import BaseEntity

class Balance(Base, BaseEntity):
    __tablename__='Balance'
    amount = Column(DECIMAL, nullable=False)
    balanceDate=Column(Date, nullable=False)
    expenseOriginId = Column(Integer, ForeignKey('ExpenseOrigin.id'), nullable=False)