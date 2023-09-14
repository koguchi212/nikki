from fire import Fire

from src.database.seeding import seeding_to_blog, seeding_to_user

from src.database.database import engine

def seeding(
    user: bool = True,
    blog: bool = True,
) -> None:
    """データベースにデータを投入する関数

    Args:
        user (bool, optional): userテーブルにデータを投入するかどうか. Defaults to False.
        blog (bool, optional): blogテーブルにデータを投入するかどうか. Defaults to False.
    """
    if user:
        seeding_to_user(engine)
    if blog:
        seeding_to_blog(engine)

if __name__ == "__main__":
    Fire(seeding)
    