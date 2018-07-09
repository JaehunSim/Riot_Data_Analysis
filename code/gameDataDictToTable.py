# -*- coding: utf-8 -*-

import pandas as pd
import json
import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
home = str(Path.home())
PATH = home + "\\Desktop\\컴공 졸프\\riot_data_analysis\\"
APIKEY = "RGAPI-0416bf72-4fe9-4fd2-b6b5-057237db2a2d"
    
pd.set_option('display.height', 100)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 100)


def timelineDictToStr(dict1):
    result = ""
    list1 = list(dict1)
    list1.sort()
    for groupedTime in list1:
        result += str(round(float(dict1[groupedTime]),1)) + " "
    result = result[:-1]
    return result

def transfromDictToList(dict1):
    w = dict1
    
    gameId = w["gameId"]
    gameDuration = w["gameDuration"]
    
    if gameDuration < (60 * 10 + 1):
        return "shortGame"
    
    gameVersion = w["gameVersion"]
    queueId = w["queueId"]
    
    if queueId in [460,470]:
        return "3:3Game"
    
    player_01_account_id = w["participantIdentities"][0]["player"]["accountId"]
    player_02_account_id = w["participantIdentities"][1]["player"]["accountId"]
    player_03_account_id = w["participantIdentities"][2]["player"]["accountId"]
    player_04_account_id = w["participantIdentities"][3]["player"]["accountId"]
    player_05_account_id = w["participantIdentities"][4]["player"]["accountId"]
    player_06_account_id = w["participantIdentities"][5]["player"]["accountId"]
    player_07_account_id = w["participantIdentities"][6]["player"]["accountId"]
    player_08_account_id = w["participantIdentities"][7]["player"]["accountId"]
    player_09_account_id = w["participantIdentities"][8]["player"]["accountId"]
    player_10_account_id = w["participantIdentities"][9]["player"]["accountId"]
    
    player_01_championId = w["participants"][0]["championId"]
    player_02_championId = w["participants"][1]["championId"]
    player_03_championId = w["participants"][2]["championId"]
    player_04_championId = w["participants"][3]["championId"]
    player_05_championId = w["participants"][4]["championId"]
    player_06_championId = w["participants"][5]["championId"]
    player_07_championId = w["participants"][6]["championId"]
    player_08_championId = w["participants"][7]["championId"]
    player_09_championId = w["participants"][8]["championId"]
    player_10_championId = w["participants"][9]["championId"]
    
    player_01_roleAndLane = w["participants"][0]["timeline"]["lane"] +"-"+ w["participants"][0]["timeline"]["role"]
    player_02_roleAndLane = w["participants"][1]["timeline"]["lane"] +"-"+ w["participants"][1]["timeline"]["role"]
    player_03_roleAndLane = w["participants"][2]["timeline"]["lane"] +"-"+ w["participants"][2]["timeline"]["role"]
    player_04_roleAndLane = w["participants"][3]["timeline"]["lane"] +"-"+ w["participants"][3]["timeline"]["role"]
    player_05_roleAndLane = w["participants"][4]["timeline"]["lane"] +"-"+ w["participants"][4]["timeline"]["role"]
    player_06_roleAndLane = w["participants"][5]["timeline"]["lane"] +"-"+ w["participants"][5]["timeline"]["role"]
    player_07_roleAndLane = w["participants"][6]["timeline"]["lane"] +"-"+ w["participants"][6]["timeline"]["role"]
    player_08_roleAndLane = w["participants"][7]["timeline"]["lane"] +"-"+ w["participants"][7]["timeline"]["role"]
    player_09_roleAndLane = w["participants"][8]["timeline"]["lane"] +"-"+ w["participants"][8]["timeline"]["role"]
    player_10_roleAndLane = w["participants"][9]["timeline"]["lane"] +"-"+ w["participants"][9]["timeline"]["role"]
    
    player_01_creepsPerMinDeltas = timelineDictToStr(w["participants"][0]["timeline"]["creepsPerMinDeltas"])
    player_02_creepsPerMinDeltas = timelineDictToStr(w["participants"][1]["timeline"]["creepsPerMinDeltas"])
    player_03_creepsPerMinDeltas = timelineDictToStr(w["participants"][2]["timeline"]["creepsPerMinDeltas"])
    player_04_creepsPerMinDeltas = timelineDictToStr(w["participants"][3]["timeline"]["creepsPerMinDeltas"])	
    player_05_creepsPerMinDeltas = timelineDictToStr(w["participants"][4]["timeline"]["creepsPerMinDeltas"])	
    player_06_creepsPerMinDeltas = timelineDictToStr(w["participants"][5]["timeline"]["creepsPerMinDeltas"])	
    player_07_creepsPerMinDeltas = timelineDictToStr(w["participants"][6]["timeline"]["creepsPerMinDeltas"])	
    player_08_creepsPerMinDeltas = timelineDictToStr(w["participants"][7]["timeline"]["creepsPerMinDeltas"])
    player_09_creepsPerMinDeltas = timelineDictToStr(w["participants"][8]["timeline"]["creepsPerMinDeltas"])
    player_10_creepsPerMinDeltas = timelineDictToStr(w["participants"][9]["timeline"]["creepsPerMinDeltas"])
    
    player_01_goldPerMinDeltas = timelineDictToStr(w["participants"][0]["timeline"]["goldPerMinDeltas"])
    player_02_goldPerMinDeltas = timelineDictToStr(w["participants"][1]["timeline"]["goldPerMinDeltas"])
    player_03_goldPerMinDeltas = timelineDictToStr(w["participants"][2]["timeline"]["goldPerMinDeltas"])
    player_04_goldPerMinDeltas = timelineDictToStr(w["participants"][3]["timeline"]["goldPerMinDeltas"])
    player_05_goldPerMinDeltas = timelineDictToStr(w["participants"][4]["timeline"]["goldPerMinDeltas"])
    player_06_goldPerMinDeltas = timelineDictToStr(w["participants"][5]["timeline"]["goldPerMinDeltas"])
    player_07_goldPerMinDeltas = timelineDictToStr(w["participants"][6]["timeline"]["goldPerMinDeltas"])
    player_08_goldPerMinDeltas = timelineDictToStr(w["participants"][7]["timeline"]["goldPerMinDeltas"])
    player_09_goldPerMinDeltas = timelineDictToStr(w["participants"][8]["timeline"]["goldPerMinDeltas"])
    player_10_goldPerMinDeltas = timelineDictToStr(w["participants"][9]["timeline"]["goldPerMinDeltas"])
    
    player_01_xpPerMinDeltas = timelineDictToStr(w["participants"][0]["timeline"]["xpPerMinDeltas"])
    player_02_xpPerMinDeltas = timelineDictToStr(w["participants"][1]["timeline"]["xpPerMinDeltas"])
    player_03_xpPerMinDeltas = timelineDictToStr(w["participants"][2]["timeline"]["xpPerMinDeltas"])
    player_04_xpPerMinDeltas = timelineDictToStr(w["participants"][3]["timeline"]["xpPerMinDeltas"])
    player_05_xpPerMinDeltas = timelineDictToStr(w["participants"][4]["timeline"]["xpPerMinDeltas"])
    player_06_xpPerMinDeltas = timelineDictToStr(w["participants"][5]["timeline"]["xpPerMinDeltas"])
    player_07_xpPerMinDeltas = timelineDictToStr(w["participants"][6]["timeline"]["xpPerMinDeltas"])
    player_08_xpPerMinDeltas = timelineDictToStr(w["participants"][7]["timeline"]["xpPerMinDeltas"])
    player_09_xpPerMinDeltas = timelineDictToStr(w["participants"][8]["timeline"]["xpPerMinDeltas"])
    player_10_xpPerMinDeltas = timelineDictToStr(w["participants"][9]["timeline"]["xpPerMinDeltas"])
    
    team1_win = w["teams"][0]["win"]
    
    temp1 = w["teams"][0]["bans"]
    temp1Result = ""
    for player in temp1:
        temp1Result += (str(player["championId"]) + " ")
    temp1Result = temp1Result[:-1]
    team1_ban = temp1Result
    
    team1_baronKills = w["teams"][0]["baronKills"]
    team1_dragonKills = w["teams"][0]["dragonKills"]
    team1_inhibitorKills = w["teams"][0]["inhibitorKills"]
    team1_towerKills = w["teams"][0]["towerKills"]
    team1_firstBlood = w["teams"][0]["firstBlood"]
    team1_firstTower = w["teams"][0]["firstTower"]
    team1_firstBaron = w["teams"][0]["firstBaron"]
    
    team2_win = w["teams"][1]["win"]
    
    temp2 = w["teams"][1]["bans"]
    temp2Result = ""
    for player in temp2:
        temp2Result += (str(player["championId"]) + " ")
    temp2Result = temp2Result[:-1]
    team2_ban = temp2Result
    
    team2_baronKills = w["teams"][1]["baronKills"]
    team2_dragonKills = w["teams"][1]["dragonKills"]
    team2_inhibitorKills = w["teams"][1]["inhibitorKills"]
    team2_towerKills = w["teams"][1]["towerKills"]
    team2_firstBlood = w["teams"][1]["firstBlood"]
    team2_firstTower = w["teams"][1]["firstTower"]
    team2_firstBaron = w["teams"][1]["firstBaron"]
    
    result = [gameId ,gameDuration ,gameVersion ,queueId ,player_01_account_id ,player_02_account_id ,player_03_account_id ,player_04_account_id ,player_05_account_id ,player_06_account_id ,player_07_account_id ,player_08_account_id ,player_09_account_id ,player_10_account_id ,player_01_championId ,player_02_championId ,player_03_championId ,player_04_championId ,player_05_championId ,player_06_championId ,player_07_championId ,player_08_championId ,player_09_championId ,player_10_championId ,player_01_roleAndLane ,player_02_roleAndLane ,player_03_roleAndLane ,player_04_roleAndLane ,player_05_roleAndLane ,player_06_roleAndLane ,player_07_roleAndLane ,player_08_roleAndLane ,player_09_roleAndLane ,player_10_roleAndLane ,player_01_creepsPerMinDeltas ,player_02_creepsPerMinDeltas ,player_03_creepsPerMinDeltas ,player_04_creepsPerMinDeltas ,player_05_creepsPerMinDeltas ,player_06_creepsPerMinDeltas ,player_07_creepsPerMinDeltas ,player_08_creepsPerMinDeltas ,player_09_creepsPerMinDeltas ,player_10_creepsPerMinDeltas ,player_01_goldPerMinDeltas ,player_02_goldPerMinDeltas ,player_03_goldPerMinDeltas ,player_04_goldPerMinDeltas ,player_05_goldPerMinDeltas ,player_06_goldPerMinDeltas ,player_07_goldPerMinDeltas ,player_08_goldPerMinDeltas ,player_09_goldPerMinDeltas ,player_10_goldPerMinDeltas ,player_01_xpPerMinDeltas ,player_02_xpPerMinDeltas ,player_03_xpPerMinDeltas ,player_04_xpPerMinDeltas ,player_05_xpPerMinDeltas ,player_06_xpPerMinDeltas ,player_07_xpPerMinDeltas ,player_08_xpPerMinDeltas ,player_09_xpPerMinDeltas ,player_10_xpPerMinDeltas ,team1_win ,team1_ban ,team1_baronKills ,team1_dragonKills ,team1_inhibitorKills ,team1_towerKills ,team1_firstBlood ,team1_firstTower ,team1_firstBaron ,team2_win ,team2_ban ,team2_baronKills ,team2_dragonKills ,team2_inhibitorKills ,team2_towerKills ,team2_firstBlood ,team2_firstTower ,team2_firstBaron]
    
    return pd.Series(result)

def conversion(data,gameTypes):
    gameDataDict = pd.Series(data)
    gameDataDict2 = gameDataDict.drop_duplicates()
    gameDataDict3 = []
    for string in gameDataDict2:
        gameDataDict3.append(json.loads(string))
    
    delList = []
    for index in range(len(gameDataDict3)):
        if "gameId" not in gameDataDict3[index].keys():
            delList.append(index)
    
    count = 0
    for i in range(len(delList)):
        del(gameDataDict3[delList[i]-count])
        count+=1
    
    
    data = pd.read_excel(PATH+"DB_file\\gameDataTableForm.xlsx")
    count = 0
    for dict1 in gameDataDict3:
        print(count)
        count+=1
        transformed = transfromDictToList(dict1)
        if type(transformed) != str:
            transformed.index = data.columns
            data = data.append(transformed,ignore_index=True)        
    data.to_excel(PATH+"DB_file\\"+gameTypes+"_gameDataTable.xlsx", index=None, encoding="euc-kr")

with open(PATH + "DB_file\\KR_RANKED_FLEX_SR_data.txt", "r") as f:
    gameDataDict = f.readlines()
gameTypes = "KR_FLEX"
conversion(gameDataDict,gameTypes)

