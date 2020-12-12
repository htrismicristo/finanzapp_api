from typing import Dict
from pydantic import BaseModel


class UserInDB(BaseModel):
    username: str
    password: str
    budget: int


database_users = Dict[str, UserInDB]
database_users = {
    "hermes23": UserInDB(**{"username": "hermes23",
                            "password": "hjromerop",
                            "budget": 20000}),
    "alison12": UserInDB(**{"username": "alison12",
                            "password": "alicarom",
                            "budget": 12000}),
    "julio06": UserInDB(**{"username": "julio06",
                           "password": "torresv",
                           "budget": 34000}),
}


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
