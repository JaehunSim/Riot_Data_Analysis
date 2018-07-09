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
    #correct retrieval
    if len(str(response.json())) > 1000:
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

def getGameData(region,gameType,gameIdList,startIndex):
    #with first gameId get data from URL. Then write file without "\n".
    gameId = gameIdList[startIndex]
    URL = "https://"+str(region)+".api.riotgames.com/lol/match/v3/matches/"+str(gameId)+"?api_key="+APIKEY
    data = getDataFromURL(URL) #dict
    dataStr = json.dumps(data) #makes dict into string
    filename = str(region)+"_"+str(gameType)+"_data.txt"
    with open(filename, 'a') as f:
        #f.write("\n")
        f.write(dataStr)
        
    count = 0 #counting gameId
    
    for gameId in gameIdList[1:]:
        #print every 10 gameId
        if count % 10 == 0:
            print(count)
        count += 1
        
        URL = "https://"+str(region)+".api.riotgames.com/lol/match/v3/matches/"+str(gameId)+"?api_key="+APIKEY
        data = getDataFromURL(URL)
        #if data responses fail, then write error with gameId
        if data == "error":
            with open(filename, 'a') as f:
                f.write("\n")
                f.write("error, gameId: " + gameId)     
        else:
            dataStr = json.dumps(data)
            with open(filename, 'a') as f:
                f.write("\n")
                f.write(dataStr)
          
data1 = pd.read_excel(PATH+"DB_file\\gameIdDB_split\\dataKRFlex.xlsx")
region = data1["region"][0]
gameType = data1["gameType"][0]
gameIdList = data1["gameId"]

getGameData(region,gameType,gameIdList,0)

#getGameData(region,gameType,gameIdList[temp2.index],101)
