from pydantic import BaseModel, Field, EmailStr

class UserRegister(BaseModel):
    username: str = Field (...,max_length=20, min_length=2)
    email: EmailStr
    password: str = Field(..., min_length=6)

class UserOut(BaseModel):
    id: int
    username: str
    email: str

class Login(BaseModel):
    email: EmailStr
    password: str

class LogModel(BaseModel):
    username: str
    email: str