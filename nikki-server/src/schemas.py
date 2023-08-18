from pydantic import BaseModel,Field
from typing import List, Optional


class BlogBase(BaseModel):
    title:str = Field(..., title="ブログのタイトル")
    body:str = Field(..., title="ブログの本文")

class Blog(BlogBase):
    class Config:
        orm_mode=True
        

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



class ShowBlog(BaseModel):
    title:str = Field(..., title="ブログのタイトル")
    body:str = Field(..., title="ブログの本文")
    creator:ShowUser 

    class Config:
        orm_mode=True

class Login(BaseModel):
    email:str = Field(..., title="ユーザーのメールアドレス")
    password:str = Field(..., title="ユーザーのパスワード")

class Token(BaseModel):
    access_token:str = Field(..., title="アクセストークン")
    token_type:str = Field(..., title="トークンの種類")

class TokenData(BaseModel):
    email:Optional[str]=None  