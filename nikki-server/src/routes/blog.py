from typing import List
from fastapi import Depends, APIRouter,status,HTTPException
from ..schemas import Blog, ShowBlog,User
from .. import models, oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from ..functions import blog
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
    return blog.get_all(db)    

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
    return blog.create(request,db,current_user)



@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=ShowBlog)
async def show(
        id:int,
        db:Session=Depends(get_db),
    ) -> ShowBlog:
    """
    # この関数はidでブログを取得します。
    """
    blog_logger.info(f"Fetching blog with id: {id}")
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
        
    return blog

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete(
        id:int,
        db:Session=Depends(get_db)
    ) -> None:
    """
    # この関数はidでブログを削除します。
    """
    blog_logger.info(f"Deleting blog with id: {id}")
    return blog.destroy(id, db)

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
    return blog.update(id, request, db)






