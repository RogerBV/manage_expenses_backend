from fastapi import FastAPI
from src.routers.category_router import category_router
from src.routers.expense_router import expense_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(category_router)
app.include_router(expense_router)