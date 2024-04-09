from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from prediction import heart_attack

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")


class HeartDiseaseData:
    def __init__(self, age: int, restingBP: int, cholesterol: int, maxhr: int, sex: str, chest_pain_type: str, exercise_agna: str, st_slope: str, fasting_bs: str):
        self.age = age
        self.restingBP = restingBP
        self.cholesterol = cholesterol
        self.maxhr = maxhr
        self.sex = sex
        self.chest_pain_type = chest_pain_type
        self.exercise_agna = exercise_agna
        self.st_slope = st_slope
        self.fasting_bs = fasting_bs


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict/", response_class=HTMLResponse)
async def predict(request: Request, age: int = Form(...), restingBP: int = Form(...), cholesterol: int = Form(...),
                  maxhr: int = Form(...), sex: str = Form(...), chest_pain_type: str = Form(...),
                  exercise_agna: str = Form(...), st_slope: str = Form(...), fasting_bs: str = Form(...)):

    # Call the heart_attack function with the received data
    result = heart_attack(age, restingBP, cholesterol, maxhr,
                          sex, chest_pain_type, exercise_agna, st_slope, fasting_bs)

    # Process the result or do something with it
    print(result)
    print(type(result))

    if result == 0:
        template_name = "no_heart_disease.html"
    elif result == 1:
        template_name = "heart_disease.html"

    return templates.TemplateResponse(template_name, {"request": request})
