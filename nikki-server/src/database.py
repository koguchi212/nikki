from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DATABASE_URL='sqlite:///./blog.db'

engine=create_engine(DATABASE_URL,connect_args={"check_same_thread":False})

sessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base=declarative_base()

def get_db():
    """
    データベースへの接続を確立する関数

    Yields:
        Session: DB接続用セッションオブジェクト
    """
    db=sessionLocal()

    try: 
        yield db
    finally:
        db.close()