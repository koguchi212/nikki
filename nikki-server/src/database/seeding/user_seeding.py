import sys, os
from sqlalchemy.orm import Session
sys.path.append(os.path.dirname(__file__))

from src import models
from src.database import engine

def seeding_to_user(engine):
    """userテーブルにデータを投入する関数

    Args:
        engine ([type]): [description]
    """
    with Session(bind=engine, autocommit=False, autoflush=False) as session:
        session.add(models.User(
            id=1,
            name="test_name1", 
            email="test_email1",
            password="test_password1",
        ))
        session.add(models.User(
            id=2,
            name="test_name2", 
            email="test_email2",
            password="test_password2",
        ))
        session.add(models.User(
            id=3,
            name="test_name3", 
            email="test_email3",
            password="test_password3",
        ))
        session.commit()

if __name__ == "__main__":
    seeding_to_user(engine) 
    