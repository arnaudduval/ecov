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
    """Class containing all member data"""
    id: int
    created_at: datetime
    updated_at: datetime


class MemberCreate(MemberBase):
    """Class for member creation"""


class MemberUpdate(MemberBase):
    """Class for member update"""


class LicenseBase(BaseModel):
    """Class containing base data for a license"""
    federation: Federation
    number: int


class License(LicenseBase):
    """Class containing all license data"""
    id: int
    created_at: datetime
    updated_at: datetime


class LicenseCreate(LicenseBase):
    """Class for license creation"""
    member_id: int


class MemberWithLicenses(MemberBase):
    """Class to retrieve a member with hbis licenses"""
    licenses: List[LicenseBase] = []
