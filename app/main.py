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
        "I am a rising sophomore at Cerritos College pursuing opportunities in mechanical and multidisciplinary engineering. "
        "My technical experience includes PCB design, Arduino development, Python programming, and CAD modeling, supported by my SolidWorks CSWA certification. "
        "I have worked on real engineering projects involving design, prototyping, testing, and system integration, giving me practical experience beyond the classroom. "
        "I am eager to apply my skills, learn from experienced engineers, and contribute to impactful engineering projects."
    ),
    "skills": [
        "Solidworks CSWA",
        "Python",
        "Arduino Library",
    ],
    "projects": [
        {
            "title": "EduGotchi",
            "slug": "project-a",
            "description": "Meet EduGotchi! This product was built for IEEE UCLA '26 hackathon for the track of education. EduGotchi is our solution to addictive phone screens, providing children with a fun alternative way to learn and interact with a toy. With EduGotchi, my team and I have been able to get in the finalist rounds amongst 20+ teams.",
            "specs": [
                "ESP32 Microcontroller",
                "LCD Display",
                "MPU 6050 Module",
            ],
            "how_it_works": "The EduGotchi is able to fetch questions from any particular AI it is set up to with a reasonable temperature to promote learning. It comes with 5 pre-installed questions however, upon shaking the EduGotchi it is able to generate more questions and the degree of difficulty increases with mastery.",
            "images": [
                "/static/images/Edugotchi_UCLA/EduGotchi_One.png",
                "/static/images/Edugotchi_UCLA/EduGotchi_Two.png",
            ],
            "video": "/static/images/Edugotchi_UCLA/DEMO_web.mp4",
        },
        {"title": "Project B", "slug": "project-b"},
        {"title": "Project C", "slug": "project-c"},
    ],
    "social": {
        "github": "https://github.com/abimferdous-pixel",
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

@app.get("/resume", response_class=HTMLResponse)
async def resume(request: Request):
    return templates.TemplateResponse(
        "resume.html", {"request": request, "data": PORTFOLIO_DATA}
    )

@app.get("/project/{slug}", response_class=HTMLResponse)
async def project_page(request: Request, slug: str):
    project = next((p for p in PORTFOLIO_DATA["projects"] if p["slug"] == slug), None)
    return templates.TemplateResponse(
        "project.html", {"request": request, "project": project, "data": PORTFOLIO_DATA}
    )
