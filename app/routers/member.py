"""
Router for members
"""
import datetime
from fastapi import APIRouter
from fastapi import HTTPException, Depends, status, Request
from sqlalchemy.orm import Session
from typing import List

from app.models.member import Member, License
from app.models.member import Gender
from app.schemas.member import MemberCreate, LicenseCreate, MemberWithLicenses
from app.core.database import Base, engine, get_db
from app.schemas.member import Member as MemberSchema

from app.forms.member import MemberCreateForm

from app.core.config import templates


members_views = APIRouter()



# Get all members
@members_views.get("/members/")
def list_members(db: Session = Depends(get_db)):
    members = db.query(Member).all()
    return members

# Create a teacher
@members_views.post("/members/", status_code=status.HTTP_201_CREATED)
def create_member(member: MemberCreate, db: Session = Depends(get_db)):
    db_member = Member(**member.dict())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

# Create a License for a Member
@members_views.post("/licenses/", status_code=status.HTTP_201_CREATED)
def create_license(license_data: LicenseCreate, db: Session = Depends(get_db)):
    db_license = License(**license_data.dict())
    db.add(db_license)
    db.commit()
    db.refresh(db_license)
    return db_license


# Read all subject from teacher id
@members_views.get("/member/{member_id}/alllicenses", response_model=MemberWithLicenses)
def read_member_with_licenses(*, member_id: int, db: Session = Depends(get_db)):
    member = db.get(Member, member_id)
    if not member:
        raise HTTPException(status_code=404, detail="member not found")
    return member

@members_views.get("/members/create/", include_in_schema=False)
async def member_create(request: Request,
                        db: Session = Depends(get_db)):
    return templates.TemplateResponse("create_member.html",
                                      {"request": request})

@members_views.post("/members/create/", include_in_schema=False)
async def member_create(request: Request,
                        db: Session = Depends(get_db)):
    form = MemberCreateForm(request)
    await form.load_data()
    if form.is_valid():
        try:
            member = Member(
                first_name=form.first_name,
                last_name=form.last_name,
                birthdate=datetime.datetime.strptime(form.birthdate, "%Y-%m-%d").date(),
                gender=form.gender
            )
            db.add(member)
            db.commit()
            db.refresh(member)
        except Exception as e:
            print('e=', e)
            form.__dict__.get("errors").append(
                "You might not be logged in."
            )

    return templates.TemplateResponse(request,
                                      "create_member.html",
                                       {"errors": form.errors})
