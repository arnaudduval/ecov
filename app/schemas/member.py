"""
Schema for a member
"""

from pydantic import BaseModel
from datetime import date, datetime
from app.models.member import Gender

class MemberBase(BaseModel):
    """Class containing basic data for a member"""
    first_name: str
    last_name: str
    birthdate: date
    gender: Gender

class Member(MemberBase):
    """Class containing member data"""
    id: int
    created_at: datetime
    updated_at: datetime

class MemberCreate(MemberBase):
    """Class for member creation"""
    pass

class MemberUpdate(MemberBase):
    """Class for member update"""
    pass