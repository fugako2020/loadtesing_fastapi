from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate")
async def calculate(
    request: Request,
    number1: float = Form(...),
    number2: float = Form(...),
    operation: str = Form(...)
):
    if operation == "add":
        result = number1 + number2
    elif operation == "subtract":
        result = number1 - number2
    elif operation == "multiply":
        result = number1 * number2
    elif operation == "divide":
        result = number1 / number2 if number2 != 0 else "Error: Division by zero"
    else:
        result = "Invalid operation"

    return templates.TemplateResponse("index.html", {"request": request, "result": result})

