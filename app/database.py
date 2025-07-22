from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use SQLite for simplicity
DATABASE_URL = "sqlite:///./todos.db"

# Create DB engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
