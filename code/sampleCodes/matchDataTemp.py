# -*- coding: utf-8 -*-
import requests
import pandas as pd
from pathlib import Path
import time
import warnings
warnings.filterwarnings("ignore")

def getDataFromURL(URL):
    response = requests.get(URL)
    return response.json()

home = str(Path.home())
PATH = home + "\\Desktop\\컴공 졸프\\riot_data_analysis\\"
APIKEY = "RGAPI-0416bf72-4fe9-4fd2-b6b5-057237db2a2d"

"""
match data in detail
URL3 = "https://kr.api.riotgames.com/lol/match/v3/matches/3187146213?api_key=RGAPI-9b3a8e2d-c066-4275-b78e-2dc9bd5644db"
w3 = getDataFromURL(URL3)
"""
