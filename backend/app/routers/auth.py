from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal, Base, engine
from ..models import User, RoleEnum
from ..schemas import RegisterIn, LoginIn, TokenOut
from ..utils import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

# Ensure tables exist (simple approach for this project)
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=TokenOut)
def register(payload: RegisterIn, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        email=payload.email,
        password_hash=hash_password(payload.password),
        role=RoleEnum.user
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token(sub=str(user.id), role=user.role.value)
    return TokenOut(access_token=token, role=user.role.value)

@router.post("/login", response_model=TokenOut)
def login(payload: LoginIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(sub=str(user.id), role=user.role.value)
    return TokenOut(access_token=token, role=user.role.value)
