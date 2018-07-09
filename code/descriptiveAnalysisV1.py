# -*- coding: utf-8 -*-
import numpy as np 
import pandas as pd
from getSummonerName import getSummonerName
from sklearn import preprocessing
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")

home = str(Path.home())
PATH = home + "\\Desktop\\컴공 졸프\\riot_data_analysis\\"

data = pd.read_excel(PATH+"DB_file\\KR_SOLO_gameDataTable2.xlsx")
championDB = pd.read_excel(PATH+"DB_file\\championID.xlsx")


#temp = getSummonerName("kr",data["player_01_account_id"][1])

#list(championDB[championDB["id"]==data["player_01_championId"][index]].key)[0]

championPickIndex = range(14,24)
versionIndex = 2
team1WinIndex = 64
team2WinIndex = 73
championBan1Index = 65
championBan2Index = 74
totalIndexList = [versionIndex]
for i in championPickIndex:
    totalIndexList.append(i)
for i in [team1WinIndex,team2WinIndex,championBan1Index,championBan2Index]:
    totalIndexList.append(i)
totalPickData = data.iloc[:, championPickIndex]
totalData = data.iloc[:,totalIndexList]
team1Index = [0,1,2,3,4,5,11,13]
team2Index = [0,6,7,8,9,10,12,14]
team1Data = totalData.iloc[:,team1Index]
team2Data = totalData.iloc[:,team2Index]

le = preprocessing.LabelEncoder()
le.fit(team1Data["team1_win"])
team1Data["team1_win"] = le.transform(team1Data["team1_win"])

le = preprocessing.LabelEncoder()
le.fit(team2Data["team2_win"])
team2Data["team2_win"] = le.transform(team2Data["team2_win"])

ban1 = []
ban2 = []
ban3 = []
ban4 = []
ban5 = []

for i in team1Data["team1_ban"]:
    temp = i.split(" ")
    ban1.append(int(temp[0]))
    ban2.append(int(temp[1]))
    ban3.append(int(temp[2]))
    ban4.append(int(temp[3]))
    ban5.append(int(temp[4]))
    
team1Data["ban1"] =  ban1
team1Data["ban2"] =  ban2
team1Data["ban3"] =  ban3
team1Data["ban4"] =  ban4
team1Data["ban5"] =  ban5

ban6 = []
ban7 = []
ban8 = []
ban9 = []
ban10 = []

for i in team2Data["team2_ban"]:
    temp = i.split(" ")
    ban6.append(int(temp[0]))
    ban7.append(int(temp[1]))
    ban8.append(int(temp[2]))
    ban9.append(int(temp[3]))
    ban10.append(int(temp[4]))
    
team2Data["ban1"] =  ban6
team2Data["ban2"] =  ban7
team2Data["ban3"] =  ban8
team2Data["ban4"] =  ban9
team2Data["ban5"] =  ban10

#aggregating data
data2 = pd.DataFrame(columns=["championId","win","ban","gameVersion"])

for j in range(5):
    print(j)
    for i in range(len(team1Data)):
        temp = team1Data.iloc[i,[1+j,6,8+j,0]]
        temp.index = ["championId","win","ban","gameVersion"]
        data2 = data2.append(temp,ignore_index=True)
        
for j in range(5):
    print(j)
    for i in range(len(team2Data)):
        temp = team2Data.iloc[i,[1+j,6,8+j,0]]
        temp.index = ["championId","win","ban","gameVersion"]
        data2 = data2.append(temp,ignore_index=True)
        
tempList = []
for i in data2["gameVersion"]:
    tempList.append(i[:3])
data2["version"] = tempList
data2 = data2.iloc[:,[0,1,2,4]]
#data2.to_excel("champion_win_ban.xlsx",encoding="euc-kr",index=None)

idWinDF = data2.iloc[:,[0,1]]
idWinDF.iloc[:,1] = pd.to_numeric(idWinDF.iloc[:,1])
grouped = idWinDF.groupby("championId",as_index=False)
groupedMean = grouped.mean()
#championId, win_rate, ban_rate, etc
data3 = groupedMean
data3.columns = ["championId","win_rate"]

tempList = []
for i in data3["championId"]:
    tempList.append(list(championDB[championDB["id"]==i]["key"])[0])
data3["championName"] = tempList
data3 = data3.iloc[:,[0,2,1]]

groupedCount = grouped.count()
total = len(data)
data3["pick"] = groupedCount["win"]
data3["PickRate"] = data3["pick"] / total * 100

banCount = data2["ban"].value_counts()
banCount = banCount.sort_index()
banCount.index = range(-1,len(banCount)-1)
data3["ban"] = banCount.iloc[1:]
data3["banRate"] =  data3["ban"] / total * 100

data3["win_rate"] = data3["win_rate"] * 100

data3_simple = data3.iloc[:,[1,2,4,6]]

data3_simple.to_excel("champion_rate.xlsx",encoding="euc-kr",index=None)
