# -*- coding: utf-8 -*-
import sys,os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
PATH = desktop+"\\riot_data_analysis\\"
sys.path.append(PATH+'code')
import pandas as pd

def main():
    data = pd.read_csv(PATH+"DB_file\\mainCP.csv")
    
    dataPP = pd.read_csv(PATH+"DB_file\\predictPosition.csv")
    fpd = dataPP.groupby("champion").head(1) #frequent position data
    pdata_map = pd.Series(fpd.position)
    pdata_map.index = fpd.champion.values
    #data_p = data.iloc[:,[2,3,4,5,6,7,8,9,10,11]]
    #data_position= data_p.applymap(lambda x: pdata_map[x])
    
    #data.iloc[:,[12,13,14,15,16,17,18,19,20,21]] = data_position
    
    for i in range(10):
        temp = data.iloc[:,[2+i]].applymap(lambda x:pdata_map[x])
        data.iloc[:,[12+i]] = temp.values
        
    data.to_csv(PATH+"DB_file\\main_p_pred.csv", index=None, encoding="euc-kr")
