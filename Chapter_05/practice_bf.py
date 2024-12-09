from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr, Field
from passlib.context import CryptContext
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from probables import BloomFilter
from contextlib import asynccontextmanager

app = FastAPI()

# Ініціалізація фільтра Блума
email_filter = BloomFilter(1000000, 0.1)

# Налаштування хешування паролів
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Налаштування підключення до бази даних SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


# Модель користувача в базі даних
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)


# Модель даних для запиту реєстрації
class RegistrationRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    first_name: str
    last_name: str


# Dependency для отримання сесії бази даних
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Завантаження існуючих email з бази даних до фільтра Блума
def load_emails_to_bloom_filter(db: Session):
    emails = db.query(User.email).all()
    for email in emails:
        email_filter.add(email[0])


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    try:
        load_emails_to_bloom_filter(db)
        yield
    finally:
        db.close()


app = FastAPI(lifespan=lifespan)


@app.post("/register")
async def register_user(request: RegistrationRequest, db: Session = Depends(get_db)):
    email = request.email

    # Перевірка, чи email уже існує у фільтрі Блума
    if email_filter.check(email):
        # Email може існувати (false positive) - виконання запиту до бази даних для точної перевірки
        user = db.query(User).filter(User.email == email).first()
        if user:
            raise HTTPException(status_code=400, detail="Email already exists")

    # Хешування пароля перед збереженням
    hashed_password = pwd_context.hash(request.password)

    # Створення нового користувача
    new_user = User(
        email=email,
        password=hashed_password,
        first_name=request.first_name,
        last_name=request.last_name,
    )

    # Додавання нового користувача до бази даних
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Додавання email до фільтра Блума після успішної реєстрації
    email_filter.add(email)

    return {"message": "User registered successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
