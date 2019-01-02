# -*- coding: utf-8 -*-
import requests
import pandas as pd
import os
import datetime
import time
from pathlib import Path

import warnings
warnings.filterwarnings("ignore")

APIKEY = "RGAPI-0416bf72-4fe9-4fd2-b6b5-057237db2a2d"
LOCALE = "ko_KR"
import sys
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
PATH = desktop+"\\riot_data_analysis\\"
sys.path.append(PATH+'code')
#URL에서 json파일 형식 받아오기
def getDataFromURL(URL):
    response = requests.get(URL)
    #time.sleep(0.8)
    count = 0
    #correct retrieval
    if len(str(response.json())) > 1000:
        return response.json()
    #if rate limit exceeds, then try 5 more times, for each time sleep 10 secs.
    else:
        while(response.json()["status"]["status_code"]==429):
            if count >= 10:
                return "error"
            time.sleep(15)
            response = requests.get(URL)
            time.sleep(0.8)
            if len(str(response.json())) > 1000:
                return response.json()
            count +=1
        time.sleep(3)
        response = requests.get(URL)
        return response.json()

def create_tier_list(region,gameType,tier):
    print(region,gameType,tier)
    #region: kr, na1..., gameType:RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT, tier: challenger, master
    #DB 생성시간 check
    try :
        originalDB = os.path.getmtime(PATH+"\\DB_file\\best_summoner\\"+region+"_"+gameType+"_"+tier+"List.xlsx")
    except:
        originalDB = 100000000
    creationTime = datetime.datetime.fromtimestamp(originalDB)
    now = datetime.datetime.now()

    #DB가 생성된지 300분이상이면 api call하기
    #(과부하 방지 및 속도 개선)
    if ((now - creationTime).total_seconds() / 60) > 300:
        print("getting new %s list..." % tier)
        URL = "https://"+region+".api.riotgames.com/lol/league/v3/"+tier+"leagues/by-queue/"+gameType+"?api_key="+APIKEY
        tierIDList = getDataFromURL(URL)
        if tierIDList["entries"] == []:
            return
        #받아온 json data Dataframe으로 만들기
        data = tierIDList["entries"]
        DF = pd.DataFrame(data)
        DF = DF.sort_values(by="leaguePoints",ascending=False)
        
        DF2 = DF.iloc[:,[3,4,5,6,9]]
        DF2.columns = ["LP","losses","summoner_id","summoner_name","wins"]
        DF2["rank_order"] = list(range(1,len(DF)+1))
        DF2["tier"] = tier.upper() + " - I"
        DF2 = DF2.iloc[:,[5,3,2,6,0,4,1]]
        DF2.to_excel(PATH+"\\DB_file\\best_summoner\\"+region+"_"+gameType+"_"+tier+"List.xlsx", index=None, encoding="euc-kr")
        print("champion data retrieval completed...")
        time.sleep(10)
        
def main():
    regionList = ["KR","NA1","EUN1","EUW1"]
    for region in regionList:
        print("start")
        create_tier_list(region,"RANKED_SOLO_5x5","challenger")
        create_tier_list(region,"RANKED_SOLO_5x5","master")
        create_tier_list(region,"RANKED_FLEX_SR","challenger")
        create_tier_list(region,"RANKED_FLEX_SR","master")
