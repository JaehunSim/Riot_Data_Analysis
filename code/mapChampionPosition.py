# -*- coding: utf-8 -*-
import sys,os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
PATH = desktop+"\\riot_data_analysis\\"
sys.path.append(PATH+'code')
import pandas as pd

def main():
    data = pd.read_csv(PATH+"DB_file\\main.csv")
    
    #데이터 챔피언명과 맵핑시키기
    cdata = pd.read_excel(PATH+"DB_file\\championId.xlsx")
    cdata = cdata.loc[:,["id","key"]]
    cdata_map = pd.Series(cdata.key)
    cdata_map.index = cdata.id.values
    data_picks = data.iloc[:,[2,3,4,5,6,7,8,9,10,11]]
    data_champs = data_picks.applymap(lambda x: cdata_map[x])
    data.iloc[:,[2,3,4,5,6,7,8,9,10,11]] = data_champs
    
    pdata = pd.read_excel(PATH+"DB_file\\positionMap.xlsx")
    pdata_map = pd.Series(pdata.role)
    pdata_map.index = pdata.position.values
    data_p = data.iloc[:,[12,13,14,15,16,17,18,19,20,21]]
    data_position= data_p.applymap(lambda x: pdata_map[x])
    
    data.iloc[:,[12,13,14,15,16,17,18,19,20,21]] = data_position
    
    data.to_csv(PATH+"DB_file\\mainCP.csv", index=False, encoding="euc-kr")
