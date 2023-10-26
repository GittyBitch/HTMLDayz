from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    name = "Boris König"
    skills = ['cooking','begging','sleeping','eating']
    return templates.TemplateResponse("index.html", {"request": request, "name": name, "skills": skills})


