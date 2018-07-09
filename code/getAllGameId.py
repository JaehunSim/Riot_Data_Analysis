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


region = ["KR","NA1","EUW1","EUN1"]
gameType = ["RANKED_SOLO_5x5","RANKED_FLEX_SR"]
tier = ["challenger", "master"]

def getAllGameId(region, gameType, tier):
    #get accountId from best_summonerV2 files
    filename = region + "_"+ gameType + "_"+ tier+ "List.xlsx"
    data = pd.read_excel(PATH+"DB_file\\best_summonerV2\\"+filename)
    
    #get gameIdDB
    dataGameId = pd.read_excel(PATH+"DB_file\\gameIdDB2.xlsx")

    #tracking accountId_index
    count = 0
    
    #for each accountId, get matches and from matches, get gameId. Then add it to dataGameId. 
    for accountId in data["accountId"]:
        print("region, gameType, tier, accountId, count: ", region, gameType, tier, accountId, count)
        #tracking match_index
        count2 = 0
        count+= 1
        #tracking duplicates
        existCount = 0
        
        URL = "https://"+region+".api.riotgames.com/lol/match/v3/matchlists/by-account/"+str(accountId)+"?api_key="+APIKEY
        #try data parsing, when if fail, skip if statement(go to next accountId)
        success = False
        try:
            dataFront = getDataFromURL(URL)
            time.sleep(0.8)
            success = True
        except:
            #data retrival failed; success = False
            pass
        if success:
            endIndex = dataFront["totalGames"]
            for matches in dataFront["matches"]:
                if matches["gameId"] not in dataGameId["gameId"].values:
                    if count2 % 30 == 0:
                        print("region, gameType, tier, accountId, count2: ", region, gameType, tier, accountId, count2)
                    count2 += 1
                    #save gameId in temp, add it to dataGameId.
                    temp = pd.Series([region,gameType,matches["gameId"]])
                    temp.index = dataGameId.columns
                    dataGameId = dataGameId.append(temp, ignore_index=True)
                else:
                    if existCount % 20 == 0:
                        print("exist")
                    existCount += 1
            #first hundred game record retrival is done, up to next hundred game record will be retrived
            
            if endIndex >= 100:
                beginIndex = 100
                if endIndex >= 200:
                    endIndex =  199
                URL2 = "https://"+region+".api.riotgames.com/lol/match/v3/matchlists/by-account/"+str(accountId)+"?beginIndex="+str(beginIndex)+"&endIndex="+str(endIndex)+"&api_key="+APIKEY
                
                #data retrival success2 var
                success2 = False
                try:
                    dataBack = getDataFromURL(URL2)
                    time.sleep(0.8)
                    success2 = True
                except:
                    #data retrival failed; success2 = False
                    pass
                if success2:
                    for matches in dataBack["matches"]:            
                        if matches["gameId"] not in dataGame 
                                print("region, gameType, tier, accountId, count2: ", region, gameType, tier, accountId, count2)
                            count2+=1 
                            #save gameId in temp, add it to dataGameId.
                            temp = pd.Series([region,gameType,matches["gameId"]])
                            temp.index = dataGameId.columns
                            dataGameId = dataGameId.append(temp, ignore_index=True)
                        else:
                            if existCount % 20 == 0:
                                print("exist")
                            existCount += 1
    #for the final data, save it.
    dataGameId.to_excel(PATH+"DB_file\\gameIdDB2.xlsx", index=None, encoding="euc-kr")
"""
getAllGameId(region[0],gameType[0],tier[0])
getAllGameId(region[0],gameType[1],tier[0])
getAllGameId(region[1],gameType[0],tier[0])
getAllGameId(region[1],gameType[1],tier[0])
getAllGameId(region[2],gameType[0],tier[0])
getAllGameId(region[2],gameType[1],tier[0])
getAllGameId(region[3],gameType[0],tier[0])
getAllGameId(region[3],gameType[1],tier[0])
"""



