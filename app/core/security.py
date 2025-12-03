from datetime import datetime, timedelta
from typing import Any, Union

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext

from app.core.config import settings 
from app.exceptions.common import *

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/login")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """평문 비밀번호 vs 해시 비교"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """비밀번호 해시 생성"""
    return pwd_context.hash(password)


def create_access_token(
    subject: Union[str, int],
    expires_delta: timedelta | None = None,
    extra_claims: dict[str, Any] | None = None,
) -> str:
    """JWT 액세스 토큰 생성"""
    to_encode: dict[str, Any] = extra_claims.copy() if extra_claims else {}
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))

    to_encode.update({"sub": str(subject), "exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECURITY_SECRET_KEY, algorithm=settings.SECURITY_ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> dict[str, Any]:
    """JWT 디코드 (검증 실패 시 예외 발생)"""
    try:
        payload = jwt.decode(token, settings.SECURITY_SECRET_KEY, algorithms=[settings.SECURITY_ALGORITHM])
    except JWTError as e:
        raise e
    return payload


def get_current_user_id(token: str = Depends(oauth2_scheme)) -> int:
    try:
        payload = decode_token(token)
        user_id = payload.get("sub")
        
        if user_id is None:
            raise NotFoundException
        
        return user_id
        
    except JWTError as e:
        raise e


        
