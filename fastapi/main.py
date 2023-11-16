from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount the "static" directory to serve static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create an instance of the JinjaTemplates class
templates = Jinja2Templates(directory="templates")


@app.get("/", response_model=str)
async def home(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse(
        "index.html", {"request": request, "name": "World"}
    )
