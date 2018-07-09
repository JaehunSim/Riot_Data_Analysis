# -*- coding: utf-8 -*-

#현재 working directory 설정
import sys
PATH = "C:\\Users\\tapu1\\Desktop\\컴공 졸프\\riot_data_analysis\\"
sys.path.append(PATH+'code')
import getChampionIDList
import getBestSummonersStats
from getAccountIDBySummonerID import getAccountID

import pandas as pd
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

region = "KR"
gameType = "RANKED_SOLO_5x5"
tier = "challenger"
file = region + "_" + gameType + "_" + tier + "List.xlsx"
data = pd.read_excel(PATH+"\\DB_file\\best_summoner\\"+file)

accountIdList = []
count = 0
for summoner_id in data["summoner_id"]:
    print (summoner_id, count)
    count += 1
    accountIdList.append(getAccountID(region,str(summoner_id)))

data["accountId"] = accountIdList
data = data.iloc[:,[0,1,2,-1,3,4,5,6]]
data.to_excel(PATH+"\\DB_file\\best_summonerV2\\"+file)

accountIdDB = data.iloc[:,[2,3]]
accountIdDB["region"] = region
accountIdDB = accountIdDB.iloc[:,[-1,0,1]]
accountIdDB.to_excel(PATH+"\\DB_file\\"+"accountIdDB.xlsx", index=None, encoding="euc-kr")
