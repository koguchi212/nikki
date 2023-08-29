from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import models, token
from src.database import get_db
from .. hashing import verify_password
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.log import get_logger


auth_logger = get_logger(category="AUTH")


router=APIRouter(
    tags=['Auth']
)

@router.post('/login')
async def login(request:OAuth2PasswordRequestForm=Depends(), db:AsyncSession=Depends(get_db)):
    async with db as session:  # 非同期セッションを直接使用
        # クエリを作成
        stmt = select(models.User).filter(models.User.email == request.username)

        # クエリを実行し、結果を取得
        result = await session.execute(stmt)

        # ユーザーを取得
        user = result.scalar()
    if not user:
        auth_logger.info(f'emailの認証情報が無効です: {request.username}')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid Credentials')
    if not verify_password(request.password,user.password):   
        auth_logger.info(f'emailのパスワードが間違っています: {request.username}')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Incorrect password') 

    access_token=token.create_access_token(
        data={"sub":user.email, "id":user.id}
    )
    auth_logger.info(f'emailの認証に成功しました: {request.username}')
    return {"access_token":access_token, "token_type":"bearer"}
