# -*- coding: utf-8 -*-
import sys,os
import pandas as pd
PATH = os.path.dirname(os.path.realpath(sys.argv[0]))[:-5]
sys.path.append(PATH+'\\code')

data = pd.read_csv(PATH+"\\DB_file\\main_finalV3.csv", engine="python")
data2 = data.iloc[:,[2,3,4,5,6,7,8,9,10,11,14]]

popList = []
for i in range(5):
    dataList = []
    temp = data2.iloc[:,[0+i,-1]]
    temp.columns = [temp.iloc[:,0].name[6:],"Win"]
    dataList.append(temp)
    temp = data2.iloc[:,[5+i,-1]]
    temp.iloc[:,1] = temp.iloc[:,1].apply(lambda x: 1-x)
    temp.columns = [temp.iloc[:,0].name[6:],"Win"]
    dataList.append(temp)
    
    data3 = pd.concat(dataList)
    
    data4 = data3.iloc[:,0]
    data5 = data4.value_counts(ascending=False)
    data6 =data5[71:]
    popList.append(list(data6.index))
        
popIndexList = []
for j in range(5):
    for i in range(len(data.iloc[:,2+j])):
        if data.iloc[:,2+j][i] in popList[j]:
            popIndexList.append(i)
for j in range(5):
    for i in range(len(data.iloc[:,7+j])):
        if data.iloc[:,7+j][i] in popList[j]:
            popIndexList.append(i)            


data_f = data.drop(popIndexList)
data_f.to_csv(PATH+"DB_file\\dropped_dataV2.csv", index=None)
