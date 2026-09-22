import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Par défaut, utilise votre base locale.
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:allerenavant@localhost:5433/ged_db"
)

# Correction automatique du préfixe exigé par SQLAlchemy
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Seul "sslmode" est un argument de connexion valide pour psycopg2
connect_arguments = {}
if "supabase.co" in DATABASE_URL:
    connect_arguments["sslmode"] = "require"

engine = create_engine(
    DATABASE_URL, 
    connect_args=connect_arguments
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dépendance pour obtenir la session de BDD dans les routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Par défaut, utilise votre base locale.
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:allerenavant@localhost:5433/ged_db"
)

# Correction automatique du préfixe exigé par SQLAlchemy
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Seul "sslmode" est un argument de connexion valide pour psycopg2
connect_arguments = {}
if "supabase.co" in DATABASE_URL:
    connect_arguments["sslmode"] = "require"

engine = create_engine(
    DATABASE_URL, 
    connect_args=connect_arguments
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dépendance pour obtenir la session de BDD dans les routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
