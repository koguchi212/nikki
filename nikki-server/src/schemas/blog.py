from pydantic import BaseModel,Field



class BlogBase(BaseModel):
    title:str = Field(..., title="ブログのタイトル")
    body:str = Field(..., title="ブログの本文")

class Blog(BlogBase):
    class Config:
        orm_mode=True


class ShowBlog(BaseModel):
    title:str = Field(..., title="ブログのタイトル")
    body:str = Field(..., title="ブログの本文")
    

    class Config:
        orm_mode=True