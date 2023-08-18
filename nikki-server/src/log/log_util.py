import os, dotenv
from logging import getLogger, FileHandler, Formatter, DEBUG
from enum import Enum

dotenv.load_dotenv(override=True)


class LogCategory(Enum):
    USER = "user.log"
    BLOG = "blog.log"
    AUTH = "auth.log"
    OTHER = "other.log"


def get_logger(category: str = "OTHER"):
    """loggerオブジェクトを取得する関数

    Args:
        category (str): ログ出力先カテゴリ名

        引数categoryの値は次の中から選択:\n
            - USER: User関連
            - BLOG: Blog関連
            - AUTH: Auth関連
            - OTHER: その他

    Returns:
        logging.Logger: loggerオブジェクト

    Raises:
        Exception: categoryが無効な値の場合
    """
    try:
        logger = getLogger(category)

        if os.getenv("LOGGING") != "true":
            return logger

        logger.setLevel(DEBUG)
        handler = FileHandler(f"./src/log/logs/{LogCategory[category].value}", encoding='utf-8')
        handler.setLevel(DEBUG)
        handler.setFormatter(Formatter("%(levelname)-9s  %(asctime)s  [%(filename)s:%(lineno)d] %(message)s"))
        logger.addHandler(handler)
        return logger

    except KeyError:
        raise Exception(
    f"""InvalidCategoryError: 
    category="{category}"は無効な値です。
    引数"category"は次の中から選択してください:
    {list(LogCategory.__members__.keys())}
    """
        )


def get_test_logger(category: str = "TEST"):
    """test用loggerオブジェクトを取得する関数

    Args:
        category (str): ログ出力先カテゴリ名

    Returns:
        logging.Logger: loggerオブジェクト
    """
    logger = getLogger("TEST")
    return logger