from pydantic import BaseModel
from datetime import datetime


class TransactionIn(BaseModel):
    username: str
    value: int
    category: str


class TransactionOut(BaseModel):
    id: int
    username: str
    date: datetime
    actual_budget: int

    class Config:
        orm_mode = True
