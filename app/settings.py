import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool
    DATABASE_URL: str

    class Config:
        env_file = os.getenv("CONFIG_FILE", ".env")
