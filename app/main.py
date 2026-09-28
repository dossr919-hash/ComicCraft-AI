from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os, base64, uuid
from app.ai.gemini_flash import generate_comic

app = FastAPI()

# Vercel la /tmp than writable
STATIC_DIR = "/tmp/static" if os.path.exists("/var/task") else "app/static"
os.makedirs(STATIC_DIR, exist_ok=True)

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    story = data.get("story", "")
    images = generate_comic(story) # this returns list
    return {"images": images}

# Vercel needs this
# app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
