# -*- coding: utf-8 -*-
import requests
import json
import pandas as pd
from pathlib import Path
import time
import warnings
import random
warnings.filterwarnings("ignore")

def getDataFromURL(URL):
    ranNum = random.randint(0,len(keyList)-1)
    URL = URL[:-42]+keyList[ranNum]
    response = requests.get(URL)
    count = 0
    #correct retrieval
    if len(str(response.json())) > 1000:
        return response.json()
    #if rate limit exceeds, then try 5 more times, for each time sleep 10 secs.
    else:
        while(response.json()["status"]["status_code"]==429):
            if count >= 10:
                return "error"
            time.sleep(3)
            ranNum = random.randint(0,len(keyList)-1)
            URL = URL[:-42]+keyList[ranNum]
            response = requests.get(URL)
#            time.sleep(0.8)
            if len(str(response.json())) > 1000:
                return response.json()
            count +=1
#        time.sleep(3)
        ranNum = random.randint(0,len(keyList)-1)
        URL = URL[:-42]+keyList[ranNum]
        response = requests.get(URL)
        return response.json()

import sys,os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
PATH = desktop+"\\riot_data_analysis\\"
sys.path.append(PATH+'code')
APIKEY = "RGAPI-0416bf72-4fe9-4fd2-b6b5-057237db2a2d" #robby1125 app
APIKEY2 = "RGAPI-d0b63723-1efc-4287-b411-e03b5a1be66d" #robby1125 
APIKEY3 = "RGAPI-1c2c1974-dc32-46ae-9932-bf6b81b576e9" #feliz
APIKEY4 = "RGAPI-d1208160-a4b4-49da-86a0-36b5db7285dc" #feliz1125
APIKEY5 = "RGAPI-6ef26d8b-f0b9-4c89-aa72-a60034bc93fc" #tapu11
APIKEY6 = "RGAPI-81e70446-2512-4309-ad15-90c2ff3733d6" #tapu12
APIKEY7 = "RGAPI-32bea64c-2b88-4efc-a00b-5fea91e8ff26" #tapu13



keyList = [APIKEY, APIKEY2, APIKEY3,APIKEY4,APIKEY5,APIKEY6,APIKEY7]
def getGameData(region,gameType,gameIdList,startIndex):
    #with first gameId get data from URL. Then write file without "\n".
    start_time = time.time()
    gameId = gameIdList[startIndex]
    URL = "https://"+str(region)+".api.riotgames.com/lol/match/v3/matches/"+str(gameId)+"?api_key="+APIKEY3
    data = getDataFromURL(URL) #dict
    dataStr = json.dumps(data) #makes dict into string
    filename = str(region)+"_"+str(gameType)+"_data.txt"
    with open(filename, 'a') as f:
        #f.write("\n")
        f.write(dataStr)
        
    count = 0 #counting gameId
    
    for gameId in gameIdList[startIndex:]:
        #print every 10 gameId
        if count % 10 == 0:
            print(filename,count)
        count += 1
        if count % 100 == 0: 
            print(time.time() - start_time)
        
        URL = "https://"+str(region)+".api.riotgames.com/lol/match/v3/matches/"+str(gameId)+"?api_key="+APIKEY3
        data = getDataFromURL(URL)
        #if data responses fail, then write error with gameId
        if data == "error":
            with open(filename, 'a') as f:
                f.write("\n")
                f.write("error, gameId: " + str(gameId))
        else:
            dataStr = json.dumps(data)
            with open(filename, 'a') as f:
                f.write("\n")
                f.write(dataStr)

def call(fileName,index=0):                
    data1 = pd.read_excel(PATH+"DB_file\\gameIdDB_split\\"+fileName+".xlsx")
    region = data1["region"][0]
    gameType = data1["gameType"][0]
    gameIdList = data1["gameId"]
    getGameData(region,gameType,gameIdList,index)

def main():
    region = ["KR","NA1","EUN1","EUW1"]
    gameType = ["Solo","Flex"]
    for r in region:
        for g in gameType:
            fileName = "data"+r+g
            call(fileName,0)
#main("dataEUN1Flex",0)

