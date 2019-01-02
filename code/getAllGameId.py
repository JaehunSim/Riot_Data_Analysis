# -*- coding: utf-8 -*-
import requests
import pandas as pd
from pathlib import Path
import time
import warnings
warnings.filterwarnings("ignore")

def getDataFromURL(URL):
    response = requests.get(URL)
    time.sleep(0.8)
    #correct retrieval
    if len(str(response.json())) > 1000:
        return response.json()
    else:
        while(response.json()["status"]["status_code"]==429):
            time.sleep(10)
            response = requests.get(URL)
            time.sleep(0.8)
            if len(str(response.json())) > 1000:
                return response.json()
        time.sleep(3)
        response = requests.get(URL)
        return response.json()
    
import sys,os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
PATH = desktop+"\\riot_data_analysis\\"
sys.path.append(PATH+'code')
APIKEY = "RGAPI-0416bf72-4fe9-4fd2-b6b5-057237db2a2d"

#region,gameType,tier = region[0],gameType[0],tier[0]
def getAllGameId(region, gameType, tier):
    #get accountId from best_summonerV2 files
    filename = region + "_"+ gameType + "_"+ tier+ "List.xlsx"
    data = pd.read_excel(PATH+"DB_file\\best_summonerV2\\"+filename)
    
    #get gameIdDB
    dataGameId = pd.read_excel(PATH+"DB_file\\gameIdDB.xlsx")

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
        
        try:
            dataFront = getDataFromURL(URL)
            endIndex = dataFront["totalGames"]
            for matches in dataFront["matches"]:
                if matches["gameId"] not in dataGameId["gameId"].values:
                    #if count2 % 30 == 0:
                        #print("region, gameType, tier, accountId, count2: ", region, gameType, tier, accountId, count2)
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
                        if matches["gameId"] not in dataGameId["gameId"]:
                            #if count2 % 30 == 0:
                                #print("region, gameType, tier, accountId, count2: ", region, gameType, tier, accountId, count2)
                            count2+=1 
                            #save gameId in temp, add it to dataGameId.
                            temp = pd.Series([region,gameType,matches["gameId"]])
                            temp.index = dataGameId.columns
                            dataGameId = dataGameId.append(temp, ignore_index=True)
                        else:
                            if existCount % 20 == 0:
                                print("exist")
                            existCount += 1
        except:
            pass
    #for the final data, save it.
    dataGameId.to_excel(PATH+"DB_file\\gameIdDB.xlsx", index=None, encoding="euc-kr")


def main():
#    region = ["KR","NA1","EUN1","EUW1"]
    region = ["EUN1","EUW1"]
    gameType = ["RANKED_SOLO_5x5","RANKED_FLEX_SR"]
    tier = ["challenger", "master"]
    for r in region:
        for g in gameType:
            for t in tier:
                if r == "EUN1":
                    if (g,t) != ("RANKED_FLEX_SR", "master"):
                        continue
                print(r,g,t)
                getAllGameId(r,g,t)


