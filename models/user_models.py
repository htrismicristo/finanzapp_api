from pydantic import BaseModel


class UserIn(BaseModel):
    username: str
    password: str
    budget = 0

# class UserSign(BaseModel):
#     username: str
#     password: str
#     budget: int


class UserOut(BaseModel):
    username: str
    budget: str

    class Config:
        orm_mode = True
