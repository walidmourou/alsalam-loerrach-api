import jwt
from datetime import datetime, timedelta
import os

def create_jwt_token(data: dict, secret: str, algorithm: str = "HS256") -> str:
    expiration = datetime.utcnow() + timedelta(hours=1)
    data.update({"exp": expiration})
    token = jwt.encode(data, secret, algorithm=algorithm)
    return token

def decode_jwt_token(token: str, secret: str, algorithms: list = ["HS256"]) -> dict:
    try:
        payload = jwt.decode(token, secret, algorithms=algorithms)
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")

def verify_jwt_token(token: str) -> bool:
    try:
        secret_key = os.getenv("SECRET_KEY")
        payload = decode_jwt_token(token, secret_key)
        return True if payload else False
    except Exception:
        return False