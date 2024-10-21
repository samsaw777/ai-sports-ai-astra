import os
from dotenv import load_dotenv
from functools import lru_cache
from pydantic_settings import BaseSettings


load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI WIZARDS LANGGRAPH SYSTEM"
    DEBUG: bool = False
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    MODEL_NAME: str = os.getenv("MODEL_NAME")

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()