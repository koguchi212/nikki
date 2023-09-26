from sqlalchemy.orm import Session
from src import crud






def test_IDでユーザーを返す(db: Session):
    result = crud.show_user(id=1,db=db)
    assert result.name == "test_name1"
    assert result.email == "test_email1"
    assert result.password == "test_password1"




def test_ユーザーを削除する(db: Session):
    result = crud.delete_user(id=1,db=db)
    assert result == 'done'
