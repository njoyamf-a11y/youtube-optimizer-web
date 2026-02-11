
import os
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/optimize", response_class=HTMLResponse)
async def optimize(request: Request, description: str = Form(...)):
    # Fake optimization (replace later with AI logic)
    optimized_title = f"🔥 {description[:50]}... | Viral Short"
    optimized_description = f"This Short is about: {description}\n\nOptimized for engagement and SEO."
    tags = "viral, youtube shorts, motivation, trending, seo"

    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": optimized_title,
        "description": optimized_description,
        "tags": tags
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
