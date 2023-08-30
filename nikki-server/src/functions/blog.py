from .. import models
from ..schemas import Blog
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import status, HTTPException

async def get_all(db:AsyncSession):
    """
    この関数はすべてのブログを取得します。

    Args:
        db (Session): これはデータベースのセッションです。

    Returns:
        [List]: これはすべてのブログを返します。
    """
    result = await db.execute(
        select(models.Blog)
        )
    blogs = result.scalars().all()
    return blogs

async def get_by_id(id:int, db:AsyncSession):
    """
    この関数はidでブログを取得します。

    Args:
        id (int): これはブログのIDです。
        db (Session): これはデータベースのセッションです。

    Returns:
        [Blog]: これはブログを返します。
    """
    result = await db.execute(
        select(models.Blog).where(models.Blog.id==id)
        )
    blog = result.scalar()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
        
    return blog


async def create(blog: Blog,db:AsyncSession, current_user)->Blog:
    """
    この関数は新しいブログを作成します。

    Args:
        blog (Blog): これはブログのリクエストです。
        db (Session): これはデータベースのセッションです。
        current_user ([type]): これは現在のユーザーです。

    Returns:
        [Blog]: これは新しいブログを返します。
    """
    user_id = [d for d in current_user]
    user_id = user_id[0]
    new_blog=models.Blog(title=blog.title,body=blog.body,user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog    

async def destroy(id:int, db:AsyncSession)->str:
    """
    この関数はブログを削除します。

    Args:
        id (int): これはブログのIDです。
        db (Session): これはデータベースのセッションです。

    Returns:
        [str]: これは削除されたことを示します。
    """
    result = await db.execute(
        select(models.Blog).where(models.Blog.id==id)
        )
    blog = result.scalar()
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not found')
    blog.delete(synchronize_session=False)
    await db.commit()
    return 'done'

async def update(id:int, request:Blog, db:AsyncSession)->str:
    """
    この関数はブログを更新します。

    Args:
        id (int): これはブログのIDです。
        request (Blog): これはブログのリクエストです。
        db (Session): これはデータベースのセッションです。

    Returns:
        [str]: これは更新されたことを示します。
    """
    result = await db.execute(
        select(models.Blog).where(models.Blog.id==id)
        )
    blog = result.scalar()
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not found')
    blog.update(request.dict())
    await db.commit()
    return 'updated'