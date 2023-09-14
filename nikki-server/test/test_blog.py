from sqlalchemy.orm import Session
from src.functions import blog
from src.database import engine
from src.schemas import Blog




def test_IDでブログを返す():
    with Session(bind=engine, autocommit=False, autoflush=False) as db:
        result = blog.get_by_id(id=1,db=db)
        assert result.title == "test_title1"
        assert result.body == "test_body1"
        assert result.user_id == 1




def test_ブログを削除する(db: Session):
    result = blog.destroy(id=1,db=db)
    assert result == 'done'