# -*- coding: utf-8 -*-
import sys,os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
PATH = desktop+"\\riot_data_analysis\\"
sys.path.append(PATH+'code')

import pandas as pd
import numpy as np
import time
import math


data = pd.read_csv(PATH+"\\DB_file\\main_p_pred.csv")
dataPP = pd.read_csv(PATH+"DB_file\\predictPosition.csv")
fpd = dataPP.groupby("champion").head(1) #frequent position data
pdata_map = pd.Series(fpd.position)
pdata_map.index = fpd.champion.values
pvm = pd.Series(fpd.prob) #posit_value_map
pvm.index = fpd.champion.values
start_time = time.time()
divisionList = [72300*i for i in range(6)]
divisionNum = 0+1+1+1+1+1
for count in range(5):
    for j in range(divisionList[0+divisionNum],len(data)):
        if j % 100 ==0:
            print(j, time.time()-start_time)
        position = {"TOP","JUN","MID","ADC","SUP"}
        w = data.iloc[j,[2,3,4,5,6,12,13,14,15,16]]
        w3 = w[5:]
        w3_values = set(w3.values)
        position = position - w3_values
        if len(position)!=0:
            w5 = np.array([0,1,2,3,4])[w3.duplicated(keep=False)]
            length = len(w5)
            small = math.inf
            for i in range(length):
                value = pvm[w[w5[i]]]
                if value < small:
                    small = value
                    smallIndex = i
            w[w5[smallIndex]+5]= np.random.choice(list(position))
            data.iloc[j,[2,3,4,5,6,12,13,14,15,16]] = w
        
        position = {"TOP","JUN","MID","ADC","SUP"}
        w2 = data.iloc[j,[7,8,9,10,11,17,18,19,20,21]]
        w4 = w2[5:]
        w4_values = set(w4.values)
        position = position - w4_values
        if len(position)!=0:
            w6 = np.array([0,1,2,3,4])[w4.duplicated(keep=False)]
            length = len(w6)
            small = math.inf
            for i in range(length):
                value = pvm[w2[w6[i]]]
                if value < small:
                    small = value
                    smallIndex = i                    
            w2[w6[smallIndex]+5]= np.random.choice(list(position))
            data.iloc[j,[7,8,9,10,11,17,18,19,20,21]] = w2
        if j % 10000 == 0:
            data.to_csv(PATH+"\\DB_file\\main_p_fill_pt"+str(divisionNum)+".csv", encoding="euc-kr", index=None)
data.to_csv(PATH+"\\DB_file\\main_p_fill_pt"+str(divisionNum)+".csv", encoding="euc-kr", index=None)