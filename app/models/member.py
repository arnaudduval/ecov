"""
Model for a member
"""

import enum
from sqlalchemy import Column, Date, String, DateTime, Integer, Enum
from sqlalchemy.sql import func

from app.core.database import Base

class Gender(enum.Enum):
    MALE = "M"
    FEMALE = "F"

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)

    first_name = Column(String)
    last_name = Column(String)

    birthdate = Column(Date)
    gender = Column(Enum(Gender))

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(),
                        onupdate=func.now())

    def __str__(self):
        return self.first_name + " " + self.last_name

