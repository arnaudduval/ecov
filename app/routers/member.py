"""
Router for members
"""
import datetime

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.member import Member
from app.schemas.member import (
    Member as MemberSchema,
    MemberCreate,
    MemberUpdate
)

from app.core.config import templates
from app.forms.member import MemberCreateForm

members_views = APIRouter()

@members_views.post("/members/",
                    response_model=MemberSchema)
async def member_create(member_create: MemberCreate,
                         db: Session = Depends(get_db)):
    print(member_create)
    member = Member(
        first_name=member_create.first_name,
        last_name=member_create.last_name,
        birthdate=member_create.birthdate,
    )
    db.add(member)
    db.commit()
    db.refresh(member)

    return member

@members_views.get("/members/create/")
async def member_create(request: Request,
                        db: Session = Depends(get_db)):
    return templates.TemplateResponse("create_member.html",
                                      {"request": request})

@members_views.post("/members/create/")
async def member_create(request: Request,
                        db: Session = Depends(get_db)):
    form = MemberCreateForm(request)
    await form.load_data()
    if form.is_valid():
        try:
            member = Member(
                first_name=form.first_name,
                last_name=form.last_name,
                birthdate=datetime.datetime.strptime(form.birthdate, "%Y-%m-%d").date()
            )
            db.add(member)
            db.commit()
            db.refresh(member)
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append(
                "You might not be logged in."
            )
    return templates.TemplateResponse(request,
                                      "create_member.html")
