from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwt_handler import verify_jwt_token

class JwtBearer(HTTPBearer):
    def __init__(self):
        super(JwtBearer, self).__init__(auto_error=True)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials:
        credentials: HTTPAuthorizationCredentials = await super(JwtBearer, self).__call__(request)
        
        if not credentials:
            raise HTTPException(status_code=403, detail="Invalid authorization token")
        
        if not credentials.scheme == "Bearer":
            raise HTTPException(status_code=403, detail="Invalid authentication scheme")
        
        if not verify_jwt_token(credentials.credentials):
            raise HTTPException(status_code=403, detail="Invalid token or expired token")
            
        return credentials.credentials