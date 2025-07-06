from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SQLITE_URI: str = "sqlite:///./backend/database.db"


settings = Settings()
