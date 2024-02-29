"""
Model for a member
"""

import enum

from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base


class Gender(enum.Enum):
    MALE = "M"
    FEMALE = "F"

class Federation(enum.Enum):
    FFC = "FFC"
    FSGT = "FSGT"
    FFVelo = "FFVélo"


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    first_name = Column(String)
    last_name = Column(String)

    birthdate = Column(Date)
    gender = Column(Enum(Gender))

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(),
                        onupdate=func.now())

    licenses = relationship("License", back_populates="member")

    def __str__(self):
        return self.first_name + " " + self.last_name


class License(Base):
    __tablename__ = "licenses"

    id = Column(Integer, primary_key=True, index=True)

    federation = Column(Enum(Federation))
    number = Column(Integer)

    member_id = Column(Integer, ForeignKey("members.id"))
    member = relationship("Member", back_populates="licenses")

    # TODO: add created_at, updtaed_at and __str__