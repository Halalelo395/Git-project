from fastapi import FastAPI, Depends, HTTPException
from app.schemas import UserRegister, UserOut, Login, LogModel
from sqlalchemy.orm import Session
from app.database import get_db, Base, engine
from app.models import Users
from app.auth import hash_password, create_access_token, authenticate_user
from sqlalchemy.exc import IntegrityError
from app.access import get_current_user

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.post("/register")
def user_register(user:UserRegister, db: Session = Depends(get_db)):
    username_exist = db.query(Users).filter(Users.username==user.username).first()
    email_exist = db.query(Users).filter(Users.email==user.email).first()
    if username_exist:
        raise HTTPException(status_code=401, detail="username already registered")
    elif email_exist:
        raise HTTPException(status_code=401, detail="email already registered")
    new_user = Users(username=user.username, email=user.email, password=hash_password(user.password))
    db.add(new_user)
    try:
       db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="email or username already exist")
    db.refresh(new_user)
    return{"message:","new user created"}

@app.get("/users", response_model=list[UserOut])
def get_users(db: Session = Depends(get_current_user)):
    users = db.query(Users).all()
    return users

@app.get("/user/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_current_user)):
    user = db.query(Users).filter(Users.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="not found")
    return user

@app.post("/login")
def login(log: Login, db: Session = Depends(get_db)):
   user = authenticate_user(db, log.email, log.password)
   if not user:
       raise HTTPException(status_code=404, detail="invalid")
   access_token = create_access_token(subject=str(user.id))
   return {"access token": access_token, "token type": "bearer"}

@app.delete("/delete/{user_id}")
def delete_user(user_id: int, db:Session = Depends(get_current_user)):
    user = db.query(Users).filter(Users.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="user is dosent exist")
    db.delete(user)
    db.commit()
    return{"message:" "user deleted"}
