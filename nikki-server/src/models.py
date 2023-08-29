from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String,ForeignKey

from src.database import Base

class User(Base):
    """ユーザーテーブル

    ユーザーを管理するテーブル

    Attributes:
        id (int): ユーザーID
        name (str): ユーザー名
        email (str): メールアドレス
        password (str): パスワード

        blogs (Blog): Blogテーブルとのリレーション
    """
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    email=Column(String(100))
    password=Column(String(100))
    
    blogs=relationship('Blog',back_populates='creator',lazy='joined')
    
class Blog(Base):
    """ブログテーブル

    ブログを管理するテーブル

    Attributes:
        id (int): ブログID
        title (str): ブログのタイトル
        body (str): ブログの本文
        user_id (int): ユーザーID

        creator (User): Userテーブルとのリレーション
    """
    __tablename__="blogs"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(100))
    body=Column(String(1024))
    user_id=Column(Integer,ForeignKey('users.id'))

    creator=relationship('User',back_populates='blogs',lazy='joined')