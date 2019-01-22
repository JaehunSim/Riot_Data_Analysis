# Riot_Data_Analysis
Using Riot API, get data, predict winning team

실행 과정
1. getBestSummonersStats : 각 지역별로 마스터, 챌린저 티어의 summonerId 호출하기
2. addAccountIDWithBestSummoner: 1번에서 호출된 summonerId의 accountId를 찾기
3. getAllGameId: 각 플레이어들이 최근 200판동앆 했던 게임의 id를 호출하기
4. splitGameID: 3번의 게임id를 지역별로 나누기
5. getGameDataFromGameID: 지역별로 나뉜 게임id로 json 형식의 게임 데이터를 호출하기
6. gameDataDictToTableV2: 5번에서 호출된 json 파일을 table형태로 가공하기
7. integrateDataTable: 지역별로 나누어짂 데이터를 통합하기
8. mapChampionPosition: 7번의 데이터에서 각 챔피언별로 포지션 선택 비율 뽑아내기
9. positionPrediction: 8번의 테이블을 이용해 7번의 데이터 중 포지션 컬럼을 가공하기
10. changePosition: 9번의 데이터를 TOP, MID, JUN, ADC, SUP 순으로 바꾸기
11. rearrayV2: 10번의 데이터를 최종 데이터로 쓸 컬럼만 뽑아내 가공하기
12. predictWin_final_v5: 최종 데이터를 이용해 모델링하기
