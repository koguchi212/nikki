from typing import List
from fastapi import Depends, APIRouter,status
from ..schemas import Blog, ShowBlog,User
from .. import models, oauth2
from sqlalchemy.orm import Session
from src.database import get_db
from src import crud
from src.log import get_logger

router=APIRouter(prefix='/blog',tags=['blogs'])


blog_logger = get_logger(category="BLOG")

@router.get('/', response_model=List[ShowBlog])
async def all_fetch(
        db:Session=Depends(get_db), 
        current_user:User=Depends(oauth2.get_current_user)
    ) -> List[ShowBlog]:
    """
    # この関数はすべてのブログを取得します。
    """
    blog_logger.info("Get all blogs!")
    return crud.get_all_blog(db, current_user)    

@router.post('/',status_code=status.HTTP_201_CREATED)
async def create(
        request: Blog,
        db:Session=Depends(get_db),
        current_user:User=Depends(oauth2.get_current_user),
    ) -> ShowBlog:
    """
    # この関数はブログを作成します。
    """
    blog_logger.info("Create blog!")
    return crud.create_blog(request,db,current_user)



@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=ShowBlog)
async def show(
        id:int,
        db:Session=Depends(get_db),
    ) -> ShowBlog:
    """
    # この関数はidでブログを取得します。
    """
    blog_logger.info(f"Fetching blog with id: {id}")

    return crud.get_blog_by_id(id, db)
        

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete(
        id:int,
        db:Session=Depends(get_db)
    ) -> None:
    """
    # この関数はidでブログを削除します。
    """
    blog_logger.info(f"Deleting blog with id: {id}")
    return crud.delete_blog(id, db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
async def update(
        id,
        request:Blog,
        db:Session=Depends(get_db)
    ) -> ShowBlog:
    """
    # この関数はidでブログを更新します。
    """
    blog_logger.info(f"Updating blog with id: {id}")
    return crud.update_blog(id, request, db)






