from sqlalchemy import Column, String, Integer
from app.database import Base

class Users(Base):
    __tablename__ = "UsersT"
    id = Column(Integer, primary_key=True, unique=True,index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
   
    