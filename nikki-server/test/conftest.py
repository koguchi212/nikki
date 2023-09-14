import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from src.models import Base
from src.main import app
from src.database import get_db
from src.log import get_test_logger, get_logger
from src.database.seeding import seeding_to_blog, seeding_to_user

test_db_url = 'sqlite:///nikki_test.sqlite3'
test_engine = sqlalchemy.create_engine(test_db_url, connect_args={"check_same_thread": False})
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
def seeding() -> None:
    """
    テスト用のDBにデータを投入する
    """
    seeding_to_user(test_engine)
    seeding_to_blog(test_engine)




@pytest.fixture(scope="function", autouse=True)
def logger() -> get_logger:
    """
    テスト用のログを返却する

    Yields:
        get_logger: テスト用のログ
     """
    app.dependency_overrides[get_logger] = lambda: get_test_logger
    yield logger




