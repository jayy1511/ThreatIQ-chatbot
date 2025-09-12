from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    JWT_SECRET: str = os.getenv("JWT_SECRET", "ThreatIQ")
    JWT_ALG: str = os.getenv("JWT_ALG", "HS256")
    VIRUSTOTAL_API_KEY: str | None = os.getenv("VIRUSTOTAL_API_KEY")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "orca-mini-3b.Q4_0.gguf")
    DB_URL: str = os.getenv("DB_URL", "sqlite:///./threatiq.db")

settings = Settings()
