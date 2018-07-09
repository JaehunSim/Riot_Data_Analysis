# -*- coding: utf-8 -*-
import requests
import json
import pandas as pd
from pathlib import Path
import time
import warnings
warnings.filterwarnings("ignore")

def getDataFromURL(URL):
    response = requests.get(URL)
    time.sleep(0.8)
    count = 0
    return response.json()

    #correct retrieval
    if len(str(response.json())) > 100:
        return response.json()
    #if rate limit exceeds, then try 5 more times, for each time sleep 10 secs.
    else:
        while(response.json()["status"]["status_code"]==429):
            if count >= 5:
                return "error"
            time.sleep(10)
            response = requests.get(URL)
            time.sleep(0.8)
            if len(str(response.json())) > 1000:
                return response.json()
            count +=1
        return response.json()

home = str(Path.home())
PATH = home + "\\Desktop\\컴공 졸프\\riot_data_analysis\\"
APIKEY = "RGAPI-0416bf72-4fe9-4fd2-b6b5-057237db2a2d"

def getSummonerName(region, accountId):
    URL = "https://"+str(region)+".api.riotgames.com/lol/summoner/v3/summoners/by-account/"+str(accountId)+"?api_key="+APIKEY
    result = getDataFromURL(URL)
    return result
    
def getMatchData(region, accountId):
    URL = "https://"+str(region)+".api.riotgames.com/lol/match/v3/matchlists/by-account/"+str(accountId)+"?api_key="+APIKEY
    result = getDataFromURL(URL)
    return result    
    
#w = getSummonerName("kr",210483502)
#w2 = getMatchData("kr",5055139)