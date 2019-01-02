# -*- coding: utf-8 -*-
import requests
import time
import warnings
import pandas as pd
from pathlib import Path
import sys, os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
PATH = desktop+"\\riot_data_analysis\\"
warnings.filterwarnings("ignore")


APIKEY = "RGAPI-0416bf72-4fe9-4fd2-b6b5-057237db2a2d"

def getDataFromURL(URL):
    response = requests.get(URL)
    #time.sleep(0.8)
    count = 0
    #correct retrieval
    if len(str(response.json())) > 100:
        return response.json()
    #if rate limit exceeds, then try 5 more times, for each time sleep 10 secs.
    else:
        while True:
            try:
                while(response.json()["status"]["status_code"]==429):
                    if count >= 10:
                        return "error"
                    time.sleep(15)
                    response = requests.get(URL)
                    time.sleep(0.8)
                    if len(str(response.json())) > 100:
                        return response.json()
                    count +=1
                time.sleep(3)
                response = requests.get(URL)
                return response.json()
            except:
                time.sleep(5)
                response = requests.get(URL)
                if len(str(response.json())) > 100:
                    return response.json()            

def getAccountID(region,summonerID):
    data = pd.read_excel(PATH+"DB_file\\accountIdDB.xlsx")
    data2 = data[data["region"]==region]
    if int(summonerID) in data2["summoner_id"].values:
        return data2[data2["summoner_id"]==int(summonerID)]["accountId"].values[0]
    
    #if there's no key in IdDB, add it and return accountId
    URL = "https://"+region+".api.riotgames.com/lol/summoner/v3/summoners/"+str(summonerID)+"?api_key="+APIKEY
    urlData = getDataFromURL(URL)
    #time.sleep(0.1)
    
    #update
    temp = pd.Series([region,summonerID,urlData["accountId"]])
    temp.index = data.columns
    data = data.append((temp),ignore_index=True)
    data.to_excel(PATH+"DB_file\\accountIdDB.xlsx", index=None, encoding="euc-kr")

    return urlData["accountId"]

#w = getAccountID("EUW1", 51828174,0)
