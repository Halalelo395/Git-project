import os
import bcrypt
import hashlib
from pathlib import Path
from dotenv import load_dotenv
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from app.models import Users
from sqlalchemy.orm import Session

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR/".env")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRY_MINUTES = 15

if not SECRET_KEY:
    raise ValueError("secret key not found")

pwd_context = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(subject: str, expire_delta: timedelta | None = None)-> str:
    expire = datetime.now(timezone.utc) + (expire_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES))
    to_encode = {"sub": subject, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY,algorithm=ALGORITHM)

def decode_access_token(token: str)-> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None

def authenticate_user(db: Session, email:str, password: str):
    user = db.query(Users).filter(Users.email==email).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user