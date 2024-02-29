"""
Database management
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.orm import registry



from app.core.config import settings

engine = create_engine(
    settings.SQLITE_URL,
    connect_args={"check_same_thread": False}
)

# TODO: Useful when using sqlite  ???
connection = engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# TODO: Is call to registry useful ??
reg = registry()
class Base(DeclarativeBase):
    registry = reg

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
