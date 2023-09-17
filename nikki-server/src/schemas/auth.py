from pydantic import BaseModel,Field
from typing import  Optional



class Login(BaseModel):
    email:str = Field(..., title="ユーザーのメールアドレス")
    password:str = Field(..., title="ユーザーのパスワード")

class Token(BaseModel):
    access_token:str = Field(..., title="アクセストークン")
    token_type:str = Field(..., title="トークンの種類")

class TokenData(BaseModel):
    email:Optional[str]=None  