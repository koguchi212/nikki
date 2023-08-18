from fastapi import  status,HTTPException
from ..schemas import User
from .. import models
from sqlalchemy.orm import Session
from ..hashing import Hash


def create(request:User,db:Session)->User:
    """
    この関数は新しいユーザーを作成します。

    Args:
        request (User): これはユーザーのリクエストです。

    Returns:
        [User]: これは新しいユーザーを返します。

    """
    new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int, db:Session)->User:
    """
    この関数はユーザーを表示します。

    Args:
        id (int): これはユーザーのIDです。

    Returns:
        [User]: これはユーザーを返します。

    """
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with the id {id} is not available')
        
    return user



def destroy(id:int, db:Session)->str:
    """
    この関数はユーザーを削除します。

    Args:
        id (int): これはユーザーのIDです。

    Returns:
        [str]: これは削除されたことを示します。

    """
    user=db.query(models.User).filter(models.User.id==id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not found')
    user.delete(synchronize_session=False)
    db.commit()
    return 'done'
