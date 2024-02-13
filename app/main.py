from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict
from app.model import __version__ as version

app = FastAPI()


class PredictionOut(BaseModel):
    red_win: float
    chances: list[float] = []


class Teams(BaseModel):
    team_red: list[int] = []
    team_blue: list[int] = []


@app.get("/")
def home():
    return {"everything is": "OK", "model_version": version}


@app.post("/predict", response_model=PredictionOut)
def prediction(team: Teams):
    prediction, chances = predict(team.team_red, team.team_blue)
    return {"red_win": prediction, 
            "chances": chances}
