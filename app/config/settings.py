from dotenv import load_dotenv
from typing import Final
import os

# Validation Envs
class EnvException(Exception):
    pass

load_dotenv()

def validate_env(key_env: str) -> str | int:
    if value := os.getenv(key_env):
        return int(value) if value.isdigit() else value 
    raise EnvException(f"This key '{key_env}' not found in .env!")

# BACKEND ENVIROMENTS
API_HOST: Final[str] = validate_env('API_HOST')
API_PORT: Final[int] = validate_env('API_PORT')