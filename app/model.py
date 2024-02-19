import pickle
import numpy as np
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve().parent

with open(f"{BASE_DIR}/model-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

def predict(team_red: list, team_blue: list):
    champions = np.array(team_red + team_blue)
    print(champions)
    pred = model.predict(champions.reshape(1, -1))
    chance = model.predict_proba(champions.reshape(1, -1))
    flat_chances = [item for sublist in chance for item in sublist]
    return pred.item(), flat_chances

