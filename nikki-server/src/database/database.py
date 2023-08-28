import os
import dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

#環境変数を読み込む
dotenv.load_dotenv(override=True)


#DBのURL要素を環境変数から取得する
DB_PORT=os.environ.get('DB_PORT')

#DBのURLを作成する
if DB_PORT:
    SQLALCHEMY_DATABASE_URL = f"mysql+aiomysql://root@db:{DB_PORT}/demo?charset=utf8"
else:
    raise ValueError("DB_PORT must be set in environment variables.")





#DB接続エンジンを作成
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

#SessionLocalクラスを作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

#モデルのベースクラスを作成
Base = declarative_base()

#DBセッションを取得する関数
async def get_db():
    async with SessionLocal() as session:
        yield session

