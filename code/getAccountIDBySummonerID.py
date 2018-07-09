# -*- coding: utf-8 -*-
import requests
import time
import warnings
import pandas as pd
from pathlib import Path
home = str(Path.home())
PATH = home + "\\Desktop\\컴공 졸프\\riot_data_analysis\\"
warnings.filterwarnings("ignore")


APIKEY = "RGAPI-0416bf72-4fe9-4fd2-b6b5-057237db2a2d"

def getDataFromURL(URL):
    response = requests.get(URL)
    return response.json()

def getAccountID(region,summonerID):
    data = pd.read_excel(PATH+"DB_file\\accountIdDB.xlsx")
    data2 = data[data["region"]==region]
    if int(summonerID) in data2["summoner_id"].values:
        return data2[data2["summoner_id"]==int(summonerID)]["accountId"].values[0]
    
    #if there's no key in IdDB, add it and return accountId
    URL = "https://"+region+".api.riotgames.com/lol/summoner/v3/summoners/"+str(summonerID)+"?api_key="+APIKEY
    urlData = getDataFromURL(URL)
    time.sleep(0.8)
    
    #update
    temp = pd.Series([region,summonerID,urlData["accountId"]])
    temp.index = data.columns
    data = data.append((temp),ignore_index=True)
    data.to_excel(PATH+"DB_file\\accountIdDB.xlsx", index=None, encoding="euc-kr")

    return urlData["accountId"]

#w = getAccountID("EUW1", 51828174,0)
