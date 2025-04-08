from pydantic import Field
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # App
    PROJECT_NAME: str = "Flights Microservice"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # API
    API_V1_STR: str = "/api/v1"
    ALLOWED_ORIGINS: List[str] = ["*"]

    # Database
    MONGODB_URI: str = Field(..., env="MONGODB_URI")
    DB_NAME: str = "flights-reserves"

    # Other Services (microservice endpoints, etc.)
    FLIGHT_SERVICE_URL: str = "http://localhost:8000"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
