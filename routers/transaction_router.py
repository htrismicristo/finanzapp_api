from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.user_db import UserInDB
from db.transaction_db import TransactionInDB
from models.user_models import UserIn, UserOut
from models.transaction_models import TransactionIn, TransactionOut

router = APIRouter()


@router.put("/user/transaction/", response_model=TransactionOut)
async def make_transaction(transaction_in: TransactionIn,
                           db: Session = Depends(get_db)):
    user_in_db = db.query(UserInDB).get(transaction_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if transaction_in.category == "expense":
        user_in_db.budget = user_in_db.budget - transaction_in.value
    elif transaction_in.category == "income":
        user_in_db.budget = user_in_db.budget + transaction_in.value
    db.commit()
    db.refresh(user_in_db)
    transaction_in_db = TransactionInDB(**transaction_in.dict(),
                                        actual_budget=user_in_db.budget)
    db.add(transaction_in_db)
    db.commit()
    db.refresh(transaction_in_db)
    return transaction_in_db
