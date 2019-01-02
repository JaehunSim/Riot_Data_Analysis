# -*- coding: utf-8 -*-
from pathlib import Path
import sys,os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
PATH = desktop+"\\riot_data_analysis\\"
sys.path.append(PATH+'code')
import pandas as pd

def main():
    data = pd.read_csv(PATH+"DB_file\\mainCP.csv")
    data2 = data.iloc[:,[2,12]]
    data2.groupby("player_01_championId")["player_01_roleAndLane"].apply(lambda x:x.value_counts().index[0])
    dataList = []
    for i in range(10):
        temp = data.iloc[:,[2+i,12+i]]
        temp.columns = ["championId", "roleAndLane"]
        dataList.append(temp)
    data5 = pd.concat(dataList)
    w2 = data5.groupby("championId")["roleAndLane"].apply(lambda x:x.value_counts(normalize=True))
    
    w2.name = "percent"
    
    w2.to_csv(PATH+ "\\DB_file\\predictPosition.csv", encoding="euc-kr")
    data = pd.read_csv(PATH+"DB_file\\predictPosition.csv", header=None)
    data.columns = ["champion","position","prob"]
    data.to_csv(PATH+ "\\DB_file\\predictPosition.csv", encoding="euc-kr", index=None)

