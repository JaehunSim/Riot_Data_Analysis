# -*- coding: utf-8 -*-
import pandas as pd
from pathlib import Path

home = str(Path.home())
PATH = home + "\\Desktop\\컴공 졸프\\riot_data_analysis\\"

data = pd.read_excel(PATH+"DB_file\\gameIdDB.xlsx")
dataKR = data[data["region"]=="KR"]
dataKRSolo = dataKR[dataKR["gameType"]=="RANKED_SOLO_5x5"]
dataKRFlex = dataKR[dataKR["gameType"]=="RANKED_FLEX_SR"]
dataKRSolo.to_excel(PATH+"DB_file\\gameIdDB_split\\dataKRSolo.xlsx", index=None, encoding="euc-kr")
dataKRFlex.to_excel(PATH+"DB_file\\gameIdDB_split\\dataKRFlex.xlsx", index=None, encoding="euc-kr")

dataNA1 = data[data["region"]=="NA1"]
dataNA1Solo = dataNA1[dataNA1["gameType"]=="RANKED_SOLO_5x5"]
dataNA1Flex = dataNA1[dataNA1["gameType"]=="RANKED_FLEX_SR"]
dataNA1Solo.to_excel(PATH+"DB_file\\gameIdDB_split\\dataNA1Solo.xlsx", index=None, encoding="euc-kr")
dataNA1Flex.to_excel(PATH+"DB_file\\gameIdDB_split\\dataNA1Flex.xlsx", index=None, encoding="euc-kr")

dataEUW1 = data[data["region"]=="EUW1"]
dataEUW1Solo = dataEUW1[dataEUW1["gameType"]=="RANKED_SOLO_5x5"]
dataEUW1Flex = dataEUW1[dataEUW1["gameType"]=="RANKED_FLEX_SR"]
dataEUW1Solo.to_excel(PATH+"DB_file\\gameIdDB_split\\dataEUW1Solo.xlsx", index=None, encoding="euc-kr")
dataEUW1Flex.to_excel(PATH+"DB_file\\gameIdDB_split\\dataEUW1Flex.xlsx", index=None, encoding="euc-kr")

dataEUN1 = data[data["region"]=="EUN1"]
dataEUN1Solo = dataEUN1[dataEUN1["gameType"]=="RANKED_SOLO_5x5"]
dataEUN1Flex = dataEUN1[dataEUN1["gameType"]=="RANKED_FLEX_SR"]
dataEUN1Solo.to_excel(PATH+"DB_file\\gameIdDB_split\\dataEUN1Solo.xlsx", index=None, encoding="euc-kr")
dataEUN1Flex.to_excel(PATH+"DB_file\\gameIdDB_split\\dataEUN1Flex.xlsx", index=None, encoding="euc-kr")