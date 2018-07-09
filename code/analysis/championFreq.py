# -*- coding: utf-8 -*-
import pandas as pd
import os
import datetime
import time

import warnings
warnings.filterwarnings("ignore")

APIKEY = "RGAPI-0416bf72-4fe9-4fd2-b6b5-057237db2a2d"
LOCALE = "ko_KR"
PATH = "C:\\Users\\tapu1\\Desktop\\컴공 졸프\\riot_data_analysis"

#data = pd.read_excel(PATH+"\\DB_file\\KR_SOLO_gameDataTable2.xlsx")
data = pd.read_excel(PATH+"\\DB_file\\KR_FLEX_gameDataTable2.xlsx")
championIdData = pd.read_excel(PATH+"\\DB_file\\championID.xlsx")

#Pick
pickedList = []
for column in data.iloc[:,[14,15,16,17,18,19,20,21,22,23]]:
    for championId in data[column]:
        pickedList.append(championId)

pickedList = pd.Series(pickedList)
pickedListCount = pickedList.value_counts()
pickedListCount = pickedListCount.sort_index()

championIDIndex = list(pickedListCount.index)
championIDDB = list(championIdData["id"])
matchIndex = []
for i in championIDIndex:
    matchIndex.append(championIDDB.index(i))
championName = []
for i in matchIndex:
    championName.append(championIdData["key"][i])

pickedListCountData = pd.DataFrame()
pickedListCountData["name"] = championName
pickedListCountData["freq"] = list(pickedListCount)

pickedListCountData = pickedListCountData.sort_values("freq",ascending=False)

#Ban
banList1 = []
for column in data.iloc[:,[65,74]]:
    for ban in data[column]:
        banList1.append(ban)
        
banList2 = []    
for bans in banList1:
    temp = bans.split(" ")
    for ban in temp:
        #print(ban)
        banList2.append(int(ban))
        
banList2 = pd.Series(banList2)
banList2Count = banList2.value_counts()
banList2Count = banList2Count.sort_index()

championIDIndex = list(banList2Count.index)
championIDDB = list(championIdData["id"])
matchIndex = []
for i in championIDIndex:
    matchIndex.append(championIDDB.index(i))
championName = []
for i in matchIndex:
    championName.append(championIdData["key"][i])
    
banListCountData = pd.DataFrame()
banListCountData["name"] = championName
banListCountData["freq"] = list(banList2Count)

banListCountData = banListCountData.sort_values("freq",ascending=False)

#temp2 = banListCountData
