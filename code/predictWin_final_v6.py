# -*- coding: utf-8 -*-
import sys,os 
PATH = os.path.dirname(os.path.realpath(sys.argv[0]))[:-5]
sys.path.append(PATH+'\\code')

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import ensemble
import sklearn
from matplotlib import pyplot as plt

data = pd.read_csv(PATH+"\\DB_file\\main_finalV3.csv", engine="python")
championData = pd.read_excel(PATH+"\\DB_file\\championID.xlsx")
scoreList = []

data3 = data.iloc[:,[2,3,4,5,6,7,8,9,10,11,14]]
X_train, X_test, y_train, y_test = train_test_split(data3.iloc[:,:-1],data3.iloc[:,-1], test_size=0.05, random_state=0)

data3 = pd.concat([X_train,y_train],axis=1)

#top to top
ptpList = []
for i in range(5):
    data2 = data3.iloc[:,[i,5+i,-1]]
    winAvg = data2.groupby(data2.columns[0]).mean()
    champList = list(winAvg.index)
    champWinList = []
    for champ in champList:
        temp = data2[data2[data2.columns[0]]==champ].groupby(data2.columns[1]).mean()
        temp = pd.Series(list(temp.values), index=temp.index)
        temp = temp.apply(lambda x:x[0])
        temp = temp.apply(lambda x: (x - np.mean(temp)) / (np.max(temp) - np.min(temp)))
        champWinList.append(temp)
    ptpList.append([champList,champWinList])

ptpDFList = []
for i in range(5):
    data2 = data3.iloc[:,[i,5+i,-1]]
    tempDF = pd.DataFrame(ptpList[i][1],index=ptpList[i][0])
    tempDF.fillna(tempDF.median(), inplace=True)
    ptpDFList.append(tempDF)
    #tempDF.to_csv(PATH+"DB_file\\"+data2.columns[0]+"vs"+data2.columns[1]+"stats.csv")
    
#position to jungle
ptpList = []
for i in range(5):
    data2 = data3.iloc[:,[i,6,-1]]
    winAvg = data2.groupby(data2.columns[0]).mean()
    champList = list(winAvg.index)
    champWinList = []
    for champ in champList:
        temp = data2[data2[data2.columns[0]]==champ].groupby(data2.columns[1]).mean()
        temp = pd.Series(list(temp.values), index=temp.index)
        temp = temp.apply(lambda x:x[0])
        temp = temp.apply(lambda x: (x - np.mean(temp)) / (np.max(temp) - np.min(temp)))
        champWinList.append(temp)
    ptpList.append([champList,champWinList])
for i in range(len(ptpList)):
    data2 = data3.iloc[:,[i,6,-1]]
    tempDF = pd.DataFrame(ptpList[i][1],index=ptpList[i][0])
    tempDF.fillna(tempDF.median(), inplace=True)
    ptpDFList.append(tempDF)

#jungle to position
ptpList = []
for i in range(5):
    data2 = data3.iloc[:,[1,5+i,-1]]
    winAvg = data2.groupby(data2.columns[0]).mean()
    champList = list(winAvg.index)
    champWinList = []
    for champ in champList:
        temp = data2[data2[data2.columns[0]]==champ].groupby(data2.columns[1]).mean()
        temp = pd.Series(list(temp.values), index=temp.index)
        temp = temp.apply(lambda x:x[0])
        temp = temp.apply(lambda x: (x - np.mean(temp)) / (np.max(temp) - np.min(temp)))
        champWinList.append(temp)
    ptpList.append([champList,champWinList])
for i in range(5):
    data2 = data3.iloc[:,[1,5+i,-1]]
    tempDF = pd.DataFrame(ptpList[i][1],index=ptpList[i][0])
    tempDF.fillna(tempDF.median(), inplace=True)
    ptpDFList.append(tempDF)
    
#top to our mid, top to our adc, mid to our adc, adc to our sup
positList = [[0,2],[0,3],[2,3],[3,4],[5,7],[5,8],[7,8],[8,9]]
ptpList = []
for i,j in positList:
    data2 = data3.iloc[:,[i,j,-1]]
    winAvg = data2.groupby(data2.columns[0]).mean()
    champList = list(winAvg.index)
    champWinList = []
    for champ in champList:
        temp = data2[data2[data2.columns[0]]==champ].groupby(data2.columns[1]).mean()
        temp = pd.Series(list(temp.values), index=temp.index)
        temp = temp.apply(lambda x:x[0])
        temp = temp.apply(lambda x: (x - np.mean(temp)) / (np.max(temp) - np.min(temp)))
        champWinList.append(temp)
    ptpList.append([champList,champWinList])
count = 0
for i,j in positList:
    data2 = data3.iloc[:,[i,j,-1]]
    tempDF = pd.DataFrame(ptpList[count][1],index=ptpList[count][0])
    tempDF.fillna(tempDF.median(), inplace=True)
    ptpDFList.append(tempDF)
    count +=1

championSet = set(championData.key.values)
for index, value in enumerate(ptpDFList):
    ptp = value
    for missingChamp in (championSet - set(ptp.columns)):
        ptp[missingChamp] = ptp.median().median()
    for missingChamp in (championSet - set(ptp.index)):
        ptp = ptp.append(pd.Series(name=missingChamp))
        ptp.loc[missingChamp,:] = ptp.median().median()
    ptpDFList[index] = ptp

count = 0
for ptpDF in ptpDFList:
    ptpDF.to_csv(PATH+"\\DB_file\\ptp\data_"+str(count)+".csv")
    count +=1
    
data2 = data.iloc[:,[2,3,4,5,6,7,8,9,10,11,14]]

for i in range(5):
    data_temp = data.iloc[:,[2+i,7+i]]
    posit = data2.columns[i][-3].lower()
    posit2 = data2.columns[i+5][-3].lower()
    tempList = []
    for j in range(len(data_temp)):
        tempList.append(ptpDFList[i][data_temp.iloc[j,1]][data_temp.iloc[j,0]])
    data2[posit+posit2+"s"] = tempList

for i in range(5):
    data_temp = data.iloc[:,[2+i,8]]
    posit = data2.columns[i][-3].lower()
    posit2 = data2.columns[6][-3].lower()
    tempList = []
    for j in range(len(data_temp)):
        tempList.append(ptpDFList[5+i][data_temp.iloc[j,1]][data_temp.iloc[j,0]])
    data2[posit+posit2+"s"] = tempList
    
for i in range(5):
    data_temp = data.iloc[:,[3,7+i]]
    posit = data2.columns[1][-3].lower()
    posit2 = data2.columns[5+i][-3].lower()
    tempList = []
    for j in range(len(data_temp)):
        tempList.append(ptpDFList[10+i][data_temp.iloc[j,1]][data_temp.iloc[j,0]])
    data2[posit+posit2+"s"] = tempList
    
count = 0
for j,k in positList:
    data_temp = data.iloc[:,[j+2,k+2]]
    posit = data2.columns[j][-3].lower()
    posit2 = data2.columns[k][-3].lower()
    tempList = []
    for l in range(len(data_temp)):
        tempList.append(ptpDFList[15+count][data_temp.iloc[l,1]][data_temp.iloc[l,0]])
    if j>= 5:
        data2[posit+posit2+"2"] = tempList
    else:
        data2[posit+posit2+"1"] = tempList
    count +=1
    


#data3 = data2.iloc[:,[11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,10]]
#for column in data3.columns:
#    data3[column].fillna(data3[column].median(), inplace=True)
#data3.to_csv(PATH+"\\DB_file\\filteredData.csv",index=None)
data3 = pd.read_csv(PATH+"\\DB_file\\filteredData.csv", engine="python")
X_train2 = data3.iloc[X_train.index,:-1]
X_test2 = data3.iloc[X_test.index,:-1]
submit_dt = ensemble.RandomForestClassifier(n_jobs=-1)
submit_dt.set_params(max_depth= None, max_features= 'log2', n_estimators= 100, n_jobs= -1)
submit_dt.fit(X_train2, y_train)

from sklearn.externals import joblib
filename = "my_model.pkl"
joblib.dump(submit_dt, filename, compress=3)

X_test2['Win_prob'] = submit_dt.predict_proba(X_test2)[:,1]
X_test2['Win_predict'] = submit_dt.predict(X_test2.iloc[:,:-1]) 
X_test2['Win'] = y_test 

X_test['Win_prob'] = X_test2['Win_prob']
X_test['Win_predict'] = X_test2['Win_predict']
X_test['Win'] = X_test2['Win']

rejectsetList = []
data_count = []
for i in range(0,101):
    i = i*0.01
    result = X_test2[(round(i,2)<=X_test2["Win_prob"]) & (X_test2["Win_prob"]<round(i+0.01,2))]
    print(sklearn.metrics.accuracy_score(result["Win"],result['Win_predict']))
    rejectsetList.append(sklearn.metrics.accuracy_score(result["Win"],result['Win_predict']))
    data_count.append(len(result)/ len(X_test2))



results = pd.Series(rejectsetList)
results.fillna(method="bfill", inplace=True)
results.fillna(method="ffill", inplace=True)
results.name = "accuracy"
results.to_csv(PATH+"\\DB_file\\result.csv", header=True, index=None)
results_count = pd.Series(data_count)

temp = []
temp2 = []
for i in range(0,50):
    temp.append((results[i]+results[100-i])/2)
    temp2.append(results_count[i]+results_count[100-i])
temp.append(results[50])
temp2.append(results_count[50])
results = pd.Series(temp)
results_count = pd.Series(temp2)
results_count_cum = results_count.cumsum()
print(results_count.sum())
fig, ax = plt.subplots()
ax.plot(results.index,results, 'k', label='Accuracy')
ax.plot(results_count.index, results_count*10, 'b', label='count*10')
ax.set_yticks(np.arange(0, 1.1, step=0.1))
ax.set_xlabel("over 0.01*i%  or under 1 - 0.01*i%")
ax.grid()
ax.legend(loc="best")
plt.show()

plt.plot(results_count_cum)
plt.grid()
plt.show()

w = results * results_count
w2 = w.cumsum()
w3 = w2/ w2[50]
plt.plot(w2)
plt.grid()
plt.show()

loaded_model = joblib.load(filename)
games = []
games.append(["Darius", "LeeSin","Cassiopeia","Zoe", "Alistar", "Chogath","Camille", "Aatrox", "Karthus", "Pyke"])
games.append(["Aatrox", "Gragas", "Jayce", "Taliyah", "Alistar", "Viktor", "LeeSin","Irelia","Yasuo","Thresh"])
games.append(["Pyke", "Camille", "Syndra", "Vayne", "Janna", "Irelia", "LeeSin","Ryze","Sivir","Shen"])
games.append(["Lissandra", "Camille", "Leblanc", "Jinx", "Alistar", "Sion", "Pantheon","Zoe","Aatrox","Gragas"])
games.append(["Akali", "LeeSin", "Cassiopeia", "Ezreal", "Pyke", "Aatrox", "Camille","Galio","Sivir","Gragas"])

data3 = pd.DataFrame(games, 
                       columns=['team1_TOP', 'team1_JUN', 'team1_MID', 'team1_ADC', 'team1_SUP',
       'team2_TOP', 'team2_JUN', 'team2_MID', 'team2_ADC', 'team2_SUP'])
for i in range(5):
    data2 = data3.iloc[:,[i,5+i]]
    posit = data3.columns[i][-3].lower()
    posit2 = data3.columns[i+5][-3].lower()
    tempList = []
    for j in range(len(data2)):
        tempList.append(ptpDFList[i][data2.iloc[j,1]][data2.iloc[j,0]])
    data3[posit+posit2+"s"] = tempList

for i in range(5):
    data2 = data3.iloc[:,[i,6]]
    posit = data3.columns[i][-3].lower()
    posit2 = data3.columns[6][-3].lower()
    tempList = []
    for j in range(len(data2)):
        tempList.append(ptpDFList[5+i][data2.iloc[j,1]][data2.iloc[j,0]])
    data3[posit+posit2+"s"] = tempList
for i in range(5):
    data2 = data3.iloc[:,[1,5+i]]
    posit = data3.columns[1][-3].lower()
    posit2 = data3.columns[5+i][-3].lower()
    tempList = []
    for j in range(len(data2)):
        tempList.append(ptpDFList[10+i][data2.iloc[j,1]][data2.iloc[j,0]])
    data3[posit+posit2+"s"] = tempList
    
count = 0
for j,k in positList:
    data2 = data3.iloc[:,[j,k]]
    posit = data3.columns[j][-3].lower()
    posit2 = data3.columns[k][-3].lower()
    tempList = []
    for l in range(len(data2)):
        tempList.append(ptpDFList[15+count][data2.iloc[l,1]][data2.iloc[l,0]])
    if j>= 5:
        data3[posit+posit2+"2"] = tempList
    else:
        data3[posit+posit2+"1"] = tempList
    count +=1

data4 = data3.iloc[:,[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]]
winRate = loaded_model.predict_proba(data4)[:,1]

#X_test2["Win_Naive"] = 0
print(sklearn.metrics.accuracy_score(y_test,X_test2['Win_predict']))
#print(winRate[0])
#print(sklearn.metrics.accuracy_score(y_test,X_test2['Win_Naive']))
#scoreList.append(sklearn.metrics.accuracy_score(y_test,X_test2['Win_predict']))

#scoreList = [0.56236,0.56287,0.56337,0.55804,0.56287,0.56477,0.57264,0.56045,0.56007,0.56325]

             