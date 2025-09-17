from pydantic import BaseModel, EmailStr, Field

class PersonBase(BaseModel):
    email: EmailStr
    full_name: str | None = Field(default=None, min_length=3)
