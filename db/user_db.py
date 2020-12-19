from typing import Dict
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from db.db_connection import Base, engine


# class UserInDB(BaseModel):
#     username: str
#     password: str
#     balance: int

class UserInDB(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, unique=True)
    password = Column(String)
    budget = Column(Integer)


Base.metadata.create_all(bind=engine)

# database_users = Dict[str, UserInDB]
# database_users = {
#     "hermes23": UserInDB(**{"username": "hermes23",
#                             "password": "hjromerop",
#                             "budget": 20000}),
#     "alison12": UserInDB(**{"username": "alison12",
#                             "password": "alicarom",
#                             "budget": 12000}),
#     "julio06": UserInDB(**{"username": "julio06",
#                            "password": "torresv",
#                            "budget": 34000}),
# }


def get_user(username: str):

    if username in database_users.keys():
        return database_users[username]
    else:
        return None


def create_user(new_user: UserInDB):
    database_users[new_user.username] = new_user


def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db
