from pydantic import BaseModel, EmailStr


class SignupRequest(BaseModel):
    email: EmailStr
    password: str


class SignupResponse(BaseModel):
    ok: bool = True


class LoginRequest(SignupRequest):
    pass


class LoginResponse(SignupResponse):
    pass
