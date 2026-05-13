from pydantic import BaseModel
import os

class Settings(BaseModel):
    app_name: str = os.getenv("APP_NAME", "Audit Assistant API")
    secret_key: str = os.getenv("SECRET_KEY", "change_me")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./audit_assistant.db")

settings = Settings()
