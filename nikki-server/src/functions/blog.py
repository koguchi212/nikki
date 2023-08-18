from .. import models
from ..schemas import Blog
from sqlalchemy.orm import Session
from fastapi import status, HTTPException

def get_all(db:Session):
    """
    この関数はすべてのブログを取得します。

    Args:
        db (Session): これはデータベースのセッションです。

    Returns:
        [List]: これはすべてのブログを返します。
    """
    blogs=db.query(models.Blog).all()
    return blogs

def create(blog: Blog,db:Session, current_user)->Blog:
    """
    この関数は新しいブログを作成します。

    Args:
        blog (Blog): これはブログのリクエストです。
        db (Session): これはデータベースのセッションです。
        current_user ([type]): これは現在のユーザーです。

    Returns:
        [Blog]: これは新しいブログを返します。
    """
    user_id=[d for d in current_user]
    user_id=user_id[0].id
    new_blog=models.Blog(title=blog.title,body=blog.body,user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog    

def destroy(id:int, db:Session)->str:
    """
    この関数はブログを削除します。

    Args:
        id (int): これはブログのIDです。
        db (Session): これはデータベースのセッションです。

    Returns:
        [str]: これは削除されたことを示します。
    """
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int, request:Blog, db:Session)->str:
    """
    この関数はブログを更新します。

    Args:
        id (int): これはブログのIDです。
        request (Blog): これはブログのリクエストです。
        db (Session): これはデータベースのセッションです。

    Returns:
        [str]: これは更新されたことを示します。
    """
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not found')
    blog.update(request.dict())
    db.commit()
    return 'updated'