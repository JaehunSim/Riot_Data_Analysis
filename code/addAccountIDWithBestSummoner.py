# -*- coding: utf-8 -*-

#현재 working directory 설정
from pathlib import Path
import sys,os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
PATH = desktop+"\\riot_data_analysis\\"
sys.path.append(PATH+'code')
from getAccountIDBySummonerID import getAccountID
import pandas as pd
import time

APIKEY = "RGAPI-0416bf72-4fe9-4fd2-b6b5-057237db2a2d"

pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

def addAccountID(region,gameType,tier):
    file = region + "_" + gameType + "_" + tier + "List.xlsx"
    data = pd.read_excel(PATH+"\\DB_file\\best_summoner\\"+file)
    accountIdList = []
    count = 0
    for summoner_id in data["summoner_id"]:
        print(summoner_id, count)
        count += 1
        accountIdList.append(getAccountID(region,str(summoner_id)))
        
    data["accountId"] = accountIdList
    data = data.iloc[:,[0,1,2,-1,3,4,5,6]]
    data.to_excel(PATH+"\\DB_file\\best_summonerV2\\"+file, index=None, encoding="euc-kr")

def main():
    region = ["KR","NA1","EUN1","EUW1"]
    gameType = ["RANKED_SOLO_5x5","RANKED_FLEX_SR"]
    tier = ["challenger", "master"]
    for r in region:
        for g in gameType:
            for t in tier:
                print(r,g,t)
                addAccountID(r,g,t)
    
#    region = ["KR","NA1","EUN1","EUW1"][0]
#    gameType = ["RANKED_SOLO_5x5","RANKED_FLEX_SR"][0]
#    tier = "challenger"
#    addAccountID(region,gameType,tier)
#    
#    region = ["KR","NA1","EUN1","EUW1"][0]
#    gameType = ["RANKED_SOLO_5x5","RANKED_FLEX_SR"][0]
#    tier = "master"
#    addAccountID(region,gameType,tier)    
#    
#    region = ["KR","NA1","EUN1","EUW1"][0]
#    gameType = ["RANKED_SOLO_5x5","RANKED_FLEX_SR"][1]
#    tier = "challenger"
#    addAccountID(region,gameType,tier)
#    
#    region = ["KR","NA1","EUN1","EUW1"][1]
#    gameType = ["RANKED_SOLO_5x5","RANKED_FLEX_SR"][0]
#    tier = "challenger"
#    addAccountID(region,gameType,tier)
#    
#    region = ["KR","NA1","EUN1","EUW1"][1]
#    gameType = ["RANKED_SOLO_5x5","RANKED_FLEX_SR"][1]
#    tier = "challenger"
#    addAccountID(region,gameType,tier)
#    
#    
#    region = ["KR","NA1","EUN1","EUW1"][2]
#    gameType = ["RANKED_SOLO_5x5","RANKED_FLEX_SR"][0]
#    tier = "challenger"
#    addAccountID(region,gameType,tier)
#    
#    region = ["KR","NA1","EUN1","EUW1"][2]
#    gameType = ["RANKED_SOLO_5x5","RANKED_FLEX_SR"][1]
#    tier = "challenger"
#    addAccountID(region,gameType,tier)
#    
#    region = ["KR","NA1","EUN1","EUW1"][3]
#    gameType = ["RANKED_SOLO_5x5","RANKED_FLEX_SR"][0]
#    tier = "challenger"
#    addAccountID(region,gameType,tier)
#    
#    region = ["KR","NA1","EUN1","EUW1"][3]
#    gameType = ["RANKED_SOLO_5x5","RANKED_FLEX_SR"][1]
#    tier = "challenger"
#    addAccountID(region,gameType,tier)
    
    import winsound
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)    
