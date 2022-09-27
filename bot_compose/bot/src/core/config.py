from dotenv import load_dotenv
from loguru import logger
from pydantic import BaseSettings

logger.add(
    'logs.log',
    format='{time} {level} {message}',
    level='DEBUG',
    rotation='10 KB',
    compression='zip',
)

load_dotenv()


class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    BOT_TOKEN: str

    REDIS_HOST: str
    REDIS_PORT: int


settings = Settings()
