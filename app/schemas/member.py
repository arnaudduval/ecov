"""
Schema for a member
"""

from pydantic import BaseModel
from datetime import date, datetime

class MemberBase(BaseModel):
    first_name: str
    last_name: str
    birthdate: date

class Member(MemberBase):
    id: int
    created_at: datetime
    updated_at: datetime

class MemberCreate(MemberBase):
    pass

class MemberUpdate(MemberBase):
    pass