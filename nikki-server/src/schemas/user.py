from pydantic import BaseModel,Field
from typing import List
from src.schemas.blog import Blog


class User(BaseModel):
    name:str = Field(..., title="ユーザーの名前")
    email:str = Field(..., title="ユーザーのメールアドレス")
    password:str = Field(..., title="ユーザーのパスワード")

class ShowUser(BaseModel):
    name:str = Field(..., title="ユーザーの名前")
    email:str = Field(..., title="ユーザーのメールアドレス")
    blogs:List[Blog]=[] 
    class Config:
        orm_mode=True
