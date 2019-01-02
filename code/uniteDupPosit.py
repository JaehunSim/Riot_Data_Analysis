# -*- coding: utf-8 -*-
import sys,os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
PATH = desktop+"\\riot_data_analysis\\"
sys.path.append(PATH+'code')

import pandas as pd
import numpy as np
import time

data0 = pd.read_csv(PATH+"\\DB_file\\main_p_fill_pt0.csv")
data0 = data0.iloc[:72300,:]
data1 = pd.read_csv(PATH+"\\DB_file\\main_p_fill_pt1.csv")
data1 = data1.iloc[72300:72300*2,:]
data2 = pd.read_csv(PATH+"\\DB_file\\main_p_fill_pt2.csv")
data2 = data2.iloc[72300*2:72300*3,:]
data3 = pd.read_csv(PATH+"\\DB_file\\main_p_fill_pt3.csv")
data3 = data3.iloc[72300*3:72300*4,:]
data4 = pd.read_csv(PATH+"\\DB_file\\main_p_fill_pt4.csv")
data4 = data4.iloc[72300*4:72300*5,:]
data5 = pd.read_csv(PATH+"\\DB_file\\main_p_fill_pt5.csv")
data5 = data5.iloc[72300*5:,:]
dataList = [data0,data1,data2,data3,data4,data5]
data = pd.concat(dataList)
data.to_csv(PATH+"\\DB_file\\main_p_fill.csv")
