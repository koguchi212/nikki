import os
import dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#環境変数を読み込む
dotenv.load_dotenv(override=True)


#DBのURL要素を環境変数から取得する
DB_PORT=os.environ.get('DB_PORT')

#DBのURLを作成する
if DB_PORT:
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root@db:{DB_PORT}/demo?charset=utf8"
else:
    raise ValueError("DB_PORT must be set in environment variables.")





#DB接続エンジンを作成
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

#SessionLocalクラスを作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#モデルのベースクラスを作成
Base = declarative_base()

#DBセッションを取得する関数
def get_db():
    """
    DBセッションを取得する関数

    Returns:
        Session: DBセッション
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
