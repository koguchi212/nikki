import os
import dotenv
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from src.models import Base
from src.main import app
from src.database import get_db
from src.log import get_test_logger, get_logger

#環境変数を読み込む
dotenv.load_dotenv(override=True)


#DBのURL要素を環境変数から取得する
DB_PORT=os.environ.get('DB_PORT')

#DBのURLを作成する
if DB_PORT:
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root@db:{DB_PORT}/test_demo?charset=utf8"
else:
    raise ValueError("DB_PORT must be set in environment variables.")

test_engine = sqlalchemy.create_engine(url=SQLALCHEMY_DATABASE_URL)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

@pytest.fixture(scope="function", autouse=True)
def db() -> Session:
    """
    テスト用のDBを返却する

    Yields:
        Session: テスト用のDB
    """
    try:
        db = TestSessionLocal()
        Base.metadata.drop_all(bind=test_engine)
        Base.metadata.create_all(bind=test_engine)
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function", autouse=True)
def client() -> TestClient:
    """
    テスト用のクライアントを返却する

   Yields:
        TestClient: テスト用のクライアント
    """
    app.dependency_overrides[get_db] = lambda: db
    with TestClient(app) as client:
        yield client
    

@pytest.fixture(scope="function", autouse=True)
def logger() -> get_logger:
    """
    テスト用のログを返却する

    Yields:
        get_logger: テスト用のログ
     """
    app.dependency_overrides[get_logger] = lambda: get_test_logger
    yield logger




