from sqlalchemy.orm import Session

from app.cores import security
from app.schemas.auth import *
from app.exceptions.auth import *
from app.repositories import user_info as user_repository


def signup_user(request: SignupRequest, db: Session) -> SignupResponse:
    existing = user_repository.get_user_by_email(db, request.email)
    if existing:
        raise DuplicatedEmailException()

    password_hash = security.get_password_hash(request.password)
    user_repository.create_user(db, request, password_hash)
    return SignupResponse()


def login_user(request: LoginRequest, db: Session) -> str:
    user = user_repository.get_user_by_email(db, request.email)
    if not user or not security.verify_password(request.password, user.password_hash):
        raise InvalidLoginException()

    return security.create_access_token(user)
