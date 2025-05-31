from src.entities.common.base import base_metadata
from src.entities.common import DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.entities import Category
from src.entities import Expense
from src.entities import ExpenseOrigin
import psycopg2

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(bind=engine)

# base_metadata.create_all(engine)