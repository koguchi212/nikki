from sqlalchemy import create_engine
import os, dotenv
from src.models import Base

#環境変数を読み込む
dotenv.load_dotenv(override=True)


#DBのURL要素を環境変数から取得する
DB_PORT=os.environ.get('DB_PORT')

DB_URL = f"mysql+aiomysql://root@db:{DB_PORT}/demo?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()