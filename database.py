import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# En local : utilise localhost. Sur Render : lira la variable DATABASE_URL.
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:allerenavant@localhost:5433/ged_db"
)

# Correction automatique exigée par SQLAlchemy
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

connect_arguments = {}
# Active le SSL uniquement si on se connecte à Supabase
if "supabase" in DATABASE_URL:
    connect_arguments["sslmode"] = "require"

engine = create_engine(
    DATABASE_URL, 
    connect_args=connect_arguments
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
