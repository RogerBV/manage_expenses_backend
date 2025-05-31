from .common.base import Base
from .common.base_entity import BaseEntity
from sqlalchemy import Column, String

class ExpenseOrigin(Base, BaseEntity):
    __tablename__='ExpenseOrigin'
    name=Column(String(50), nullable=False)