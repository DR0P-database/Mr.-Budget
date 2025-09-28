from functools import lru_cache
from dotenv import load_dotenv
import os


load_dotenv()

class Settings:
    TOKEN_BOT = os.getenv("TOKEN_BOT")
    
@lru_cache()
def get_settings():
    return Settings()

