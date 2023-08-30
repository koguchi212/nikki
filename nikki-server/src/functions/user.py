from fastapi import  status,HTTPException
from ..schemas import User
from .. import models
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..hashing import Hash


async def create(request:User,db:AsyncSession)->User:
    """
    この関数は新しいユーザーを作成します。

    Args:
        request (User): これはユーザーのリクエストです。

    Returns:
        [User]: これは新しいユーザーを返します。

    """
    new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def show(id:int, db:AsyncSession)->User:
    """
    この関数はユーザーを表示します。

    Args:
        id (int): これはユーザーのIDです。

    Returns:
        [User]: これはユーザーを返します。

    """
    result = await db.execute(
        select(models.User).where(models.User.id==id)
        )
    user = result.scalar()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with the id {id} is not available')
        
    return user



async def destroy(id:int, db:AsyncSession)->str:
    """
    この関数はユーザーを削除します。

    Args:
        id (int): これはユーザーのIDです。

    Returns:
        [str]: これは削除されたことを示します。

    """
    result = await db.execute(
        select(models.User).where(models.User.id==id)
        )
    user = result.scalar()
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not found')
    user.delete(synchronize_session=False)
    await db.commit()
    return 'done'
