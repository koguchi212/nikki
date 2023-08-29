from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import os, dotenv
from src.models import Base
from sqlalchemy.orm import sessionmaker
import asyncio





#DBのURL要素を環境変数から取得する
DB_PORT=os.environ.get('DB_PORT')

DB_URL = f"mysql+aiomysql://root@db:{DB_PORT}/demo?charset=utf8"
engine = create_async_engine(DB_URL, echo=True, pool_pre_ping=True)
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)



async def reset_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    #環境変数を読み込む
    dotenv.load_dotenv(override=True)

    DB_PORT = os.environ.get('DB_PORT')
    DB_URL = f"mysql+aiomysql://root@db:{DB_PORT}/demo?charset=utf8"

    loop = asyncio.get_event_loop()
    loop.run_until_complete(reset_database())