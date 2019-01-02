# -*- coding: utf-8 -*-
from pathlib import Path
import sys,os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
PATH = desktop+"\\riot_data_analysis\\"
sys.path.append(PATH+'code')

import getBestSummonersStats
import addAccountIDWithBestSummoner
import getAllGameId
import splitGameID
import getGameDataFromGameID
import gameDataDictToTableV2
import integrateDataTable
import mapChampionPosition
import positionPrediction
import changePosition
#import dupPositionChangeV3
import rearrayV2
#getBestSummonersStats.main()
#addAccountIDWithBestSummoner.main()
#getAllGameId.main()
#splitGameID.main()
#getGameDataFromGameID.call("dataKRSolo", 43320+82800)
#getGameDataFromGameID.call("dataNA1Solo",950+40840)
#getGameDataFromGameID.call("dataEUW1Solo",530+1520+7730+1270) #끝
#getGameDataFromGameID.call("dataEUN1Solo",530+19080+18220+13430+8790+2500+1300)
#getGameDataFromGameID.call("dataKRFlex",42710) #끝
#getGameDataFromGameID.call("dataNA1Flex") #끝
#getGameDataFromGameID.call("dataEUW1Flex",22300) #끝
#getGameDataFromGameID.call("dataEUN1Flex") #끝

#fileNameList = ["EUN1_RANKED_FLEX_SR_data.txt","EUN1_RANKED_SOLO_5x5_data.txt","NA1_RANKED_FLEX_SR_data.txt"]
#gameTypesList = ["EUN1_FLEX","EUN1_SOLO","NA1_FLEX"]
#for index in range(len(fileNameList)):
#    gameDataDictToTableV2.main(fileNameList[index],gameTypesList[index])

#integrateDataTable.main()
#mapChampionPosition.main()
#positionPrediction.main()
#changePosition.main()
#dupPositionChangeV3.main() #this is slow, so it has to be multi processed
rearrayV2.main()
