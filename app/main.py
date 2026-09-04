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
        "I am a sophomore at Cerritos College pursuing opportunities in mechanical and multidisciplinary engineering. "
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
        {
            "title": "3DOF Robotic Arm",
            "slug": "project-b",
            "wip": True,
            "description": "A 3-degree-of-freedom robotic arm designed in SolidWorks and driven by NEMA 17 stepper motors through custom 3D-printed gear reductions. It's currently operated manually via a web interface, with autonomous pick-and-place operation planned as a future phase. This project is a work in progress: CAD, printed parts, and electronics are underway, and I'm actively working through gearing, wiring, and control software.",
            "specs": [
                "NEMA 17 Stepper Motors",
                "ESP32 Microcontroller",
                "4:1 Planetary Gear Reduction",
                "3D-Printed PETG Housings",
                "Custom Stepper Driver Wiring",
                "SolidWorks CAD Design",
            ],
            "how_it_works": "Each joint is driven by a NEMA 17 stepper motor through a custom 3D-printed gear reduction, controlled by an ESP32 wired to stepper driver modules on a breadboard prototype circuit. Right now the arm is operated manually through a web interface, and I'm evaluating cycloidal drive alternatives for the shoulder joint to address torque and durability needs before adding autonomous control.",
            "images": [
                "/static/images/RoboticArm/image.png",
                "/static/images/RoboticArm/20260814_180551.jpg",
                "/static/images/RoboticArm/20260814_191128.jpg",
                "/static/images/RoboticArm/20260815_052202.jpg",
                "/static/images/RoboticArm/20260815_121131.jpg",
                "/static/images/RoboticArm/20260820_014932.jpg",
            ],
        },
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
    resume_path = os.path.join(BASE_DIR, "static", "images", "RESUME_FINAL.pdf")
    resume_version = int(os.path.getmtime(resume_path)) if os.path.exists(resume_path) else 0
    return templates.TemplateResponse(
        "resume.html",
        {"request": request, "data": PORTFOLIO_DATA, "resume_version": resume_version},
    )

@app.get("/project/{slug}", response_class=HTMLResponse)
async def project_page(request: Request, slug: str):
    project = next((p for p in PORTFOLIO_DATA["projects"] if p["slug"] == slug), None)
    return templates.TemplateResponse(
        "project.html", {"request": request, "project": project, "data": PORTFOLIO_DATA}
    )
