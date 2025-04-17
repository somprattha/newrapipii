from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="web_ui/static"), name="static")
templates = Jinja2Templates(directory="web_ui/templates")

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "voices": ["th-TH-Standard-A", "th-TH-Wavenet-A"], "expressions": ["happy", "sad", "angry", "blush"]})

if __name__ == "__main__":
    uvicorn.run("start_webui:app", host="127.0.0.1", port=8000, reload=True)
