import os

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "mysql://user:password@localhost/dbname")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30