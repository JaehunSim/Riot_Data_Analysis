# -*- coding: utf-8 -*-
import numpy as np 
import pandas as pd
from getSummonerName import getSummonerName
from sklearn import preprocessing
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")

home = str(Path.home())
PATH = home + "\\Desktop\\cs_grad_project\\riot_data_analysis\\"

data = pd.read_excel(PATH+"DB_file\\champion_win_ban.xlsx")
#data = data[data["version"]==8.8]
championDB = pd.read_excel(PATH+"DB_file\\championID.xlsx")


championIdList = data["championId"].unique()
championIdList.sort()


total_ban = data["ban"].value_counts(normalize=True)
total_ban.index = list(map(lambda x: list(championDB[championDB["id"]==x].key)[0],total_ban.index))

#championIdList=[62]
ban_id = []
for championId in championIdList:
    temp_data = data[data["championId"]==championId]
    #print(championId,len(temp_data))
    value_counts = temp_data["ban"].value_counts(normalize=True)
    #value_counts = value_counts.sort_index()
    value_counts.index = list(map(lambda x: list(championDB[championDB["id"]==x].key)[0],value_counts.index))
    champion_name = list(championDB[championDB["id"]==championId].key)[0]
    champion_position =list(championDB[championDB["id"]==championId].position)[0]
    if len(temp_data) > 250:
        #print(champion_name)
        ban_id.append({"championId":champion_name,"position":champion_position,"data":value_counts})

ban_id_compare = []
for i in ban_id:
    temp_data = i["data"]
    compare = temp_data - total_ban[temp_data.index]
    compare = compare.sort_values(ascending=False)[:3]
    ban_id_compare.append({"championId":i["championId"],"position":i["position"],"ban":compare})
    
top3_ban = pd.DataFrame(columns=["championName","position","ban1","ban2","ban3"])
for i in ban_id_compare:
    bans = i["ban"].index
    temp = pd.Series([i["championId"],i["position"],bans[0],bans[1],bans[2]], index=["championName","position","ban1","ban2","ban3"])
    #print(temp)
    top3_ban = top3_ban.append(temp,ignore_index=True)
    
ban1_posit = list(map(lambda x: list(championDB[championDB["key"]==x].position)[0],top3_ban["ban1"]))
ban2_posit = list(map(lambda x: list(championDB[championDB["key"]==x].position)[0],top3_ban["ban2"]))
ban3_posit = list(map(lambda x: list(championDB[championDB["key"]==x].position)[0],top3_ban["ban3"]))

top3_ban["ban1_posit"] = ban1_posit
top3_ban["ban2_posit"] = ban2_posit
top3_ban["ban3_posit"] = ban3_posit

ban_posit_DF = top3_ban.iloc[:,[0,1,5,6,7]]

ban_posit_comb = ban_posit_DF.iloc[:,[0,1,2]]
ban_posit_comb.columns = ["championName","position","ban_posit"]
temp_DF = ban_posit_DF.iloc[:,[0,1,3]]
temp_DF.columns = ["championName","position","ban_posit"]
temp_DF2 = ban_posit_DF.iloc[:,[0,1,4]]
temp_DF2.columns = ["championName","position","ban_posit"]

frames = [ban_posit_comb,temp_DF,temp_DF2]
ban_posit_comb = pd.concat(frames)

position_list = ["TOP","MID","JUG","ADC","SUP"]
value_count_list = []
for position in position_list:
    temp = ban_posit_comb[ban_posit_comb["position"]==position]["ban_posit"]
    temp_count = temp.value_counts()
    value_count_list.append(list(temp_count[["TOP","MID","JUG","ADC","SUP"]]))
    
posit_ban_countDF =pd.DataFrame(value_count_list,index=position_list,columns=position_list)


cIdIndexList = "58, 39, 90, 13, 43, 7, 105, 8, 163, 91, 5, 164, 223, 4, 53, 81, 134, 121, 12, 157, 44, 55, 2, 201, 113, 498, 126, 27, 497, 245, 145, 40, 202, 142, 34, 117, 69, 50, 51, 136, 24, 16, 150, 72, 412, 48, 59, 115, 268, 516, 101, 114, 154, 68, 110, 25, 14, 31, 76, 266, 78, 103, 92, 122, 89, 54, 18, 3, 41, 38, 79, 30, 86, 64, 21, 421, 104, 127, 111, 85, 141, 98, 267, 222, 29, 143, 45, 67, 17, 42, 19, 22, 84, 420, 96, 75, 102, 6, 238, 28, 57, 240, 26, 112, 11, 56, 432, 63, 15, 161, 429, 254, 203, 107, 60, 20, 80, 236, 9, 61, 131, 35, 427, 119, 82, 106, 99, 133, 33, 83, 36, 1, 77, 62, 37, 23, 10, 74, 32, 120"
cIdIndexList = cIdIndexList.split(", ")
temp = []
for i in cIdIndexList:
    temp.append(int(i))
cIdIndexList = temp
corrList = "0.233471640091068, 0.196679960251795, 0.418798811798288, 0.559622265131723, 0.50159533660294, 0.546893070811299, 0.384252599360619, 0.491963376084389, 0.456066452704629, 0.594044131466166, 0.618355213664138, 0.464180684093025, 0.44468006727693, 0.516484749498839, 0.569528297609885, 0.217914853471904, 0.0412384019201808, 0.161015694216138, 0.187605695426395, 0.0450078973206535, 0.513008111921146, 0.618174249654218, 0.740248757642351, 0.894581939438224, 0.188199845049849, 0.457711485205096, 0.300740411738452, 0.162403223866051, 0.82123288302966, 0.363205906632293, 0.552904441919693, 0.387790286636129, 0.238047971495156, 0.952244831534574, 0.327421381890972, 0.297421698383287, 0.453028791006748, 0.374213024975451, 0.360315969871617, 0.608960962963967, 0.292244007076549, 0.647490734971571, 0.353601681096584, 0.229898248423632, 0.759495328867436, 0.565146207208114, 0.407270696889099, 0.776157086248514, 0.487377983359183, 0.00401755158347621, 0.603413866035299, 0.654488636269945, 0.788649362295615, 0.412088195405096, 0.275940153930529, 0.826393493690646, 0.279531405334964, 0.118296990087281, 0.718973481704507, 0.165507381632089, 0.51695356826692, 0.298173304652692, 0.756230668626991, 0.697857645335468, 0.550765360442495, 0.628646597460492, 0.708974986499525, 0.722186262872011, 0.854115824549969, 0.639405553714549, 0.59186932696525, 0.705816168486643, 0.761105291873873, 0.756560841115051, 0.878801896387167, 0.703979994927321, 0.595262783782315, 0.976597394670657, 0.197395990572596, 0.0217435323249226, 0.148161991574184, 0.371784169498493, 0.122786530619995, 0.786221370993071, 0.582543798071166, 0.17044400090603, 0.14108860269727, 0.668753596497618, 0.431591658268843, 0.127734794291739, 0.19105746231961, 0.726088477495064, 0.0384029438293343, 0.235935520517935, 0.569439577875371, 0.395676500265767, 0.502070805891267, 0.140353111538821, 0.0652434932210859, 0.459779797720079, 0.574755989375874, 0.23254079798207, 0.470517242438045, 0.890676976249805, 0.236945302675624, 0.771160277702106, 0.295369979679921, 0.400319930805164, 0.704525996569076, 0.487878038725909, 0.526366229588315, 0.64660502470886, 0.198947358661984, 0.703735565030553, 0.620128095747591, 0.424093997879596, 0.86771730755008, 0.299347943530248, 0.747740284031841, 0.3918916312501, 0.220220646601699, 0.448764103547468, 0.340987968698194, 0.627505735187201, 0.625341832316118, 0.194743230330423, 0.194696004306898, 0.289108859361518, 0.12557659710143, 0.378744588565588, 0.419043245459886, 0.474692976784931, 0.257843776210021, 0.461422981589038, 0.185134317524311, 0.68040700310478, 0.53589707867616, 0.440895529679169, 0.220640307936711, 0.578970105164063"
corrList = corrList.split(", ")
temp = []
for i in corrList:
    temp.append(float(i))
corrList = temp

corr_DF = pd.DataFrame()
corr_DF["championId"] = cIdIndexList
corr_DF["championName"]=list(map(lambda x: list(championDB[championDB["id"]==x].key)[0],cIdIndexList))
corr_DF["pvalue_btw_win_ban"] = corrList
