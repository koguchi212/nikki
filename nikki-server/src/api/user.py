from fastapi import Depends, APIRouter,status
from ..schemas import User,ShowUser
from sqlalchemy.orm import Session
from src.database import get_db
from src import crud
from src.log import get_logger

router=APIRouter(prefix='/user',tags=['users'])

user_logger = get_logger(category="USER")



@router.post('/')
async def create_user(
        request:User,
        db:Session=Depends(get_db)
    ) -> ShowUser:
    """
    # この関数はユーザーを作成します。
    """
    user_logger.info("Create user!")
    return crud.create_user(request,db)

@router.get('/{id}',response_model=ShowUser)
async def get_user(
        id:int, 
        db:Session=Depends(get_db)
    ) -> ShowUser:
    """
    # この関数はidでユーザーを取得します。
    """
    user_logger.info(f"Fetching user with id: {id}")
    return crud.show_user(id,db)



@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete(
        id:int,
        db:Session=Depends(get_db)
    ) -> None:
    """
    # この関数はidでユーザーを削除します。
    """
    user_logger.info(f"Deleting user with id: {id}")
    return crud.delete_user(id, db)

