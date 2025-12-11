from pydantic import BaseModel, EmailStr, Field

class RegisterDto(BaseModel):
    email: EmailStr
    password: str
    full_name: str | None = None
    type_user_id: int | None = None
