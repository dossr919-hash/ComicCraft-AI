from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from app.routes import router

app = FastAPI(title="ComicCraft AI")

# API routes mattum router la irunthu eduthukalam
app.include_router(router)

# Homepage - direct-a file ah padichu anuppurom, template vendaam!
@app.get("/", response_class=HTMLResponse)
def home_page():
    html_file = Path(__file__).parent / "templates" / "index.html"
    return html_file.read_text(encoding="utf-8")

@app.get("/health")
def health():
    return {"status": "ok"}