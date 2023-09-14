from sqlalchemy.orm import Session
from src.functions import user 
from src.database import engine





def test_IDでユーザーを返す(db: Session):
    result = user.show(id=1,db=db)
    assert result.name == "test_name1"
    assert result.email == "test_email1"
    assert result.password == "test_password1"




def test_ユーザーを削除する(db: Session):
    result = user.destroy(id=1,db=db)
    assert result == 'done'
