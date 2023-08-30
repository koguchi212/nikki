from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .token import verify_token
from sqlalchemy.orm import Session
from src.database import get_db

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(token:str=Depends(oauth2_scheme), db:Session=Depends(get_db)):
    """
    この関数は現在のユーザーを取得します。

    Args:
        token (str, optional): これはトークンです。. Defaults to Depends(oauth2_scheme).
        db (Session, optional): これはデータベースのセッションです。. Defaults to Depends(get_db).

    Raises:
        HTTPException: これはHTTP例外です。

    Returns:
        [type]: これは現在のユーザーを返します。
    """
    credentials_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"www-Authenticate": "Bearer"},
    )
    result = verify_token(token, credentials_exception, db)
    return {result}

