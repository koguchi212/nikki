import os,dotenv
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from .schemas import TokenData
from sqlalchemy.orm import Session
from .functions.user import show

#環境変数を読み込む
dotenv.load_dotenv(override=True)

SECRET_KEY=os.environ.get("SECRET_KEY")
ALGORITHM=os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES=30

def create_access_token(data:dict, expires_delta:Optional[timedelta]=None)->str:
    """
    アクセストークンを作成する関数

    Args:
        data (dict): データ
        expires_delta (Optional[timedelta], optional): 期限. Defaults to None.

    Returns:
        [type]: [description]
    """
    to_encode=data.copy()
    if expires_delta:
        expire=datetime.utcnow()+expires_delta
    else:
        expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt        

def verify_token(token:str, credentials_exception, db:Session)->TokenData:
    """
    JSON Web Token (JWT) を検証し、ユーザー情報を取得します。

    この関数は、指定された SECRET_KEY と ALGORITHM を使用して提供された JWT トークンを
    復号化して正当性を検証します。トークンのペイロードからユーザーのメールアドレスと ID
    を抽出します。トークンが有効であり必要な情報を含んでいる場合、対応するユーザーデータ
    がデータベースから取得されます。

    Args:
        token (str): 検証する JWT トークン。
        credentials_exception: 認証失敗時に送出される例外オブジェクト。
        db (Session): データベースセッションオブジェクト。

    Returns:
        TokenData: ユーザーのメールアドレスや他のトークン関連データを保持するデータオブジェクト。

    Raises:
        credentials_exception: JWT の検証やユーザー情報の取得に失敗した場合に送出されます。

    Note:
        トークンの検証には SECRET_KEY と ALGORITHM の定義が必要です。

    Example:
        try:
            user_data = verify_token(token, CredentialsException, db)
            # 認証されたユーザーデータを処理する
        except CredentialsException:
            # 認証失敗を処理する
    """
    try:
        payload=jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email:str=payload.get("sub")
        id:int=payload.get("id")
        if email is None:
            raise credentials_exception
        token_data=TokenData(email=email)    
    except JWTError:
        raise credentials_exception
    user = show(id, db)
    return user    
