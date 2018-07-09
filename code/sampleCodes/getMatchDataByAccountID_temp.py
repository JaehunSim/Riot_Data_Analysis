# -*- coding: utf-8 -*-
import requests
import pandas as pd

def getDataFromURL(URL):
    response = requests.get(URL)
    return response.json()


APIKEY = "RGAPI-0416bf72-4fe9-4fd2-b6b5-057237db2a2d"
PATH = "C:\\Users\\tapu1\\Desktop\\컴공 졸프\\riot_data_analysis\\"
region = "kr"
account_num = 203870735
#account_num = 207100227
URL = "https://"+region+".api.riotgames.com/lol/match/v3/matchlists/by-account/"+str(account_num)+"?api_key="+APIKEY
w = getDataFromURL(URL)
beginIndex = 100
endIndex = w["totalGames"]
URL2 = "https://"+region+".api.riotgames.com/lol/match/v3/matchlists/by-account/"+str(account_num)+"?beginIndex="+str(beginIndex)+"&endIndex="+str(endIndex)+"&api_key="+APIKEY
w2 = getDataFromURL(URL2)
URL3 = "https://kr.api.riotgames.com/lol/match/v3/matches/3187146213?api_key=RGAPI-9b3a8e2d-c066-4275-b78e-2dc9bd5644db"
w3 = getDataFromURL(URL3)
##gameId
#queue
#champion
#role

##gameId
#gameDuration
#-gameVersion
#participantIdentities -accountId
#participants
    
    #teamId
    #championId
