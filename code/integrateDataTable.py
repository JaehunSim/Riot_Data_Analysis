# -*- coding: utf-8 -*-
import sys,os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
PATH = desktop+"\\riot_data_analysis\\"
sys.path.append(PATH+'code')
import pandas as pd

def main():
    local = ["KR","NA1","EUN1","EUW1"]
    gameType = ["SOLO","FLEX"]
    
    data = pd.read_excel(PATH+"DB_file\\gameDataTableForm.xlsx")
    for loc in local:
        for type1 in gameType:
            temp = pd.read_csv(PATH+"DB_file\\gameStatsDB\\"+loc+"_"+type1+"_gameDataTable.csv")
            data = pd.concat([data,temp], ignore_index=True)
    
    data.to_csv(PATH+"DB_file\\full_DT.csv", index= None, encoding="euc-kr")
    
    data = pd.read_csv(PATH+"DB_file\\full_DT.csv")
    columns = ["gameId","gameDuration",
               "player_01_championId","player_02_championId","player_03_championId","player_04_championId","player_05_championId","player_06_championId","player_07_championId","player_08_championId","player_09_championId","player_10_championId",
               "player_01_roleAndLane","player_02_roleAndLane","player_03_roleAndLane","player_04_roleAndLane","player_05_roleAndLane","player_06_roleAndLane","player_07_roleAndLane","player_08_roleAndLane","player_09_roleAndLane","player_10_roleAndLane",
               "team1_win","team1_ban","team2_win","team2_ban"]
    data2 = data.loc[:,columns]
    
    data2.to_csv(PATH+"DB_file\\part_DT.csv", index= None, encoding="euc-kr")
