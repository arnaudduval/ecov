"""
Form for member creation
"""

from typing import List
from datetime import date
from datetime import datetime

from fastapi import Request



class MemberCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.first_name: str
        self.last_name: str
        self.birthdate: date

    async def load_data(self):
        form = await self.request.form()
        self.first_name = form.get("first_name")
        self.last_name = form.get("last_name")
        self.birthdate = form.get("birthdate")

    def is_valid(self):
        if not self.first_name:
            self.errors.append("Un prénom est requis")
        if not self.last_name:
            self.errors.append("Un nom est requis")
        if not self.birthdate:
            self.errors.append("Une date de naissance est requise")
            try:
                res = bool(datetime.strptime(self.birthdate, "%Y-%m-%d"))
            except ValueError:
                res = False
            if not res:
                self.errors.append("Une date de naissance valide est requise")
        if not self.errors:
            return True
        return False

