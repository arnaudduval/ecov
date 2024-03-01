"""
Application entry point
"""


from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.core.database import Base, engine
from app.core.config import settings, templates
from app.routers.member import members_views


app = FastAPI()

app.mount("/public", StaticFiles(directory=settings.STATIC_FILES_DIR), name="static")

Base.metadata.create_all(bind=engine)

app.include_router(members_views, tags=["Members"])

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def root(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html"
    )
