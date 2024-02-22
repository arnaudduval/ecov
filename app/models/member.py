"""
Model for a member
"""

from sqlalchemy import Column, Date, String, DateTime, Integer
from sqlalchemy.sql import func

from app.core.database import Base

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)

    first_name = Column(String)
    last_name = Column(String)

    birthdate = Column(Date)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(),
                        onupdate=func.now())

    def __str__(self):
        return self.first_name + " " + self.last_name

