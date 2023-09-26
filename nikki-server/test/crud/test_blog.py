from sqlalchemy.orm import Session
from src import crud





def test_IDでブログを返す(db: Session):
    result = crud.get_blog_by_id(id=1,db=db)
    assert result.title == "test_title1"
    assert result.body == "test_content1"
    assert result.user_id == 1




def test_ブログを削除する(db: Session):
    result = crud.delete_blog(id=1,db=db)
    assert result == 'done'