from fastapi import FastAPI
from .api import blog, user, auth
from .database import engine
from .models import Base

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)

Base.metadata.create_all(engine)