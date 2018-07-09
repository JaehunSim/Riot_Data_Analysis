# -*- coding: utf-8 -*-
import pandas as pd
import requests
import os
import datetime

PATH = "C:\\Users\\tapu1\\Desktop\\컴공 졸프\\riot_data_analysis"
#현재 working directory 설정
os.chdir(PATH)

APIKEY = "RGAPI-0416bf72-4fe9-4fd2-b6b5-057237db2a2d"
LOCALE = "ko_KR"
championIDList_URL = "https://kr.api.riotgames.com/lol/static-data/v3/champions?locale="+LOCALE+"&dataById=false&api_key="+APIKEY


#URL에서 json파일 형식 받아오기
#data from developer.riotgames.com api
#lol-static-data-v3 / champions
def getDataFromURL(URL):
    response = requests.get(URL)
    return response.json()

#champion ID table 생성
def create_champion_ID_list():
    #DB 생성시간 check
    championIDFile = os.path.getmtime(PATH+"\\DB_file\\championID.xlsx")
    creationTime = datetime.datetime.fromtimestamp(championIDFile)
    now = datetime.datetime.now()

    #DB가 생성된지 일주일이상이면 api call하기
    #(과부하 방지 및 속도 개선)
    if (now.day - creationTime.day > 7 ):
        print("getting new champion Data...")
        championIDList = getDataFromURL(championIDList_URL)
        #받아온 json data Dataframe으로 만들기
        data = championIDList["data"]
        dataValues = list(data.values())
        championID_DF = pd.DataFrame(dataValues)
        championID_DF= championID_DF.sort_values(by="id")
        championID_DF.to_excel(PATH+"\\DB_file\\championID.xlsx", index=None, encoding="euc-kr")
        print("champion data retrieval completed...")
        
def main():
    create_champion_ID_list()
    
