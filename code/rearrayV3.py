# -*- coding: utf-8 -*-
import sys,os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
PATH = desktop+"\\riot_data_analysis\\"
sys.path.append(PATH+'code')

import pandas as pd

#def main():
data = pd.read_csv(PATH+"DB_file\\main_p_fill.csv")
#data = data.iloc[:,range(2,22)]
#data = data.sample(10)

list1 = []

def reArray(row):
    tempList = []
    w =  row[[2,3,4,5,6,12,13,14,15,16]]
    w3 = w[5:]
    w3 = w3.sort_values()
    w2 = row[[7,8,9,10,11,17,18,19,20,21]]
    w4 = w2[5:]
    w4 = w4.sort_values()
    for i in w3.index:
        tempList.append(int(i[7:9])+1)
    for i in w4.index:
        tempList.append(int(i[7:9])+1)
    for i in range(10):
        tempList.append(tempList[i]+10)
    tempList = [0,1] + tempList + [22,23,24,25]
    tempSeries = row[tempList]
    tempSeries.index = row.index
    list1.append(tempSeries)

data.apply(reArray,axis=1)
data2 = pd.DataFrame(list1)
#data2.to_csv(PATH+"DB_file\\main_position_switchV2.csv", encoding="euc-kr", index=None)
data3 = data2.iloc[:,[0,1,6,3,4,2,5,11,8,9,7,10,16,13,14,12,15,21,18,19,17,20,22,23,24,25]]
data3.to_csv(PATH+"DB_file\\main_position_switch.csv", encoding="euc-kr", index=None)

