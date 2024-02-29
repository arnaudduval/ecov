"""
Schema for a member
"""

from typing import List
from datetime import date, datetime
from pydantic import BaseModel

from app.models.member import Gender, Federation


class MemberBase(BaseModel):
    """Class containing basic data for a member"""
    first_name: str
    last_name: str
    birthdate: date
    gender: Gender

class Member(MemberBase):
    # Class containing all member data
    id: int
    created_at: datetime
    updated_at: datetime

class MemberCreate(MemberBase):
    """Class for member creation"""
    pass

class MemberUpdate(MemberBase):
    """Class for member update"""
    pass

class LicenseBase(BaseModel):
    federation: Federation
    number: int

class LicenseCreate(LicenseBase):
    member_id: int

class MemberWithLicenses(MemberBase):
    licenses: List[LicenseBase] = []
