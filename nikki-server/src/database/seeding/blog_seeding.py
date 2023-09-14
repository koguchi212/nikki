import sys, os
from sqlalchemy.orm import Session
sys.path.append(os.path.dirname(__file__))

from src import models
from src.database import engine

def seeding_to_blog(engine):
    """blogテーブルにデータを投入する関数

    Args:
        engine ([type]): [description]
    """
    with Session(bind=engine, autocommit=False, autoflush=False) as session:
        session.add(models.Blog(
            id=1,
            title="test_title1", 
            body="test_content1",
            user_id=1,
        ))
        session.add(models.Blog(
            id=2,
            title="test_title2", 
            body="test_content2",
            user_id=1,
        ))
        session.add(models.Blog(
            id=3,
            title="test_title3", 
            body="test_content3",
            user_id=2,
        ))
        session.add(models.Blog(
            id=4,
            title="test_title4", 
            body="test_content4",
            user_id=3,
        ))
        session.commit()

if __name__ == "__main__":
    seeding_to_blog(engine)        