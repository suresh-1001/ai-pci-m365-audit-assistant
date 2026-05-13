from fastapi import APIRouter, HTTPException
from app.schemas.auth import LoginRequest, TokenResponse
from app.core.security import create_access_token

router = APIRouter()

@router.post('/login', response_model=TokenResponse)
def login(payload: LoginRequest):
    if payload.email == "admin@company.com" and payload.password == "ChangeMe123!":
        token = create_access_token(subject=payload.email, role="admin")
        return TokenResponse(access_token=token)
    raise HTTPException(status_code=401, detail="Invalid credentials")
