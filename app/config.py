from pydantic import SecretStr
from pydantic_settings import BaseSettings

DOTENV_PATH = "../.env"


class Settings(BaseSettings):
    logger_level: str
    bot_token: SecretStr
    user_id: int

    class Config:
        env_file = DOTENV_PATH
        env_file_encode = "utf-8"


cfg = Settings()
