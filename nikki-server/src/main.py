from fastapi import FastAPI
from .models import Base
from src.database import engine
from .routes import blog, user, auth
import asyncio

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

# asyncio.run()を使用して非同期関数を実行
if __name__ == "__main__":
    asyncio.run(init_models())
