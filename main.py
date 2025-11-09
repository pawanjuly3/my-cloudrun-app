from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

# Serve static files like JS, CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Use templates folder for HTML
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process")
async def process_data(data: dict):
    text = data.get("text", "")
    # Example logic: convert text to uppercase
    result = text.upper()
    return {"results": result}
