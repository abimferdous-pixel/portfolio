from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

PORTFOLIO_DATA = {
    "name": "Abim Ferdous",
    "title": "Mechanical Engineering Student",
    "tagline": "Passionate about mechanical systems, PCB design, and building the future one component at a time.",
    "about": (
        "I am a rising Sophomore from Cerritos College interested in mechanical systems with experience "
        "with PCB designing, certified in Solidworks CSWA, and motivated to learn."
    ),
    "skills": [
        "Solidworks CSWA",
        "Python",
        "Arduino Library",
    ],
    "projects": [
        {
            "title": "Project Alpha",
            "description": "A real-time data dashboard built with FastAPI and WebSockets.",
            "tags": ["Python", "FastAPI", "WebSockets"],
            "slug": "project-alpha",
        },
        {
            "title": "Project Beta",
            "description": "An e-commerce platform with secure payments and inventory management.",
            "tags": ["Django", "PostgreSQL", "Stripe"],
            "slug": "project-beta",
        },
        {
            "title": "Project Gamma",
            "description": "A machine learning pipeline for sentiment analysis on social media.",
            "tags": ["Python", "scikit-learn", "NLP"],
            "slug": "project-gamma",
        },
    ],
    "social": {
        "github": "https://github.com/yourhandle",
        "linkedin": "https://www.linkedin.com/in/abim-ferdous/",
        "email": "abimferdous@gmail.com",
        "phone": "(562) 574-9446",
    },
}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "data": PORTFOLIO_DATA}
    )

@app.get("/project/{slug}", response_class=HTMLResponse)
async def project_page(request: Request, slug: str):
    project = next((p for p in PORTFOLIO_DATA["projects"] if p["slug"] == slug), None)
    return templates.TemplateResponse(
        "project.html", {"request": request, "project": project, "data": PORTFOLIO_DATA}
    )
