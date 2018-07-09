#reference URL : https://www.youtube.com/watch?v=ml0lKDU5JvY
import requests

def requestSummonerData(region, summonerName, APIKey):

    #Here is how I make my URL.  There are many ways to create these.
    
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + summonerName + "?api_key=" + APIKey
    print (URL)
    #requests.get is a function given to us my our import "requests". It basically goes to the URL we made and gives us back a JSON.
    response = requests.get(URL)
    #Here I return the JSON we just got.
    return response.json()

def requestRankedData(region, ID, APIKey):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + APIKey
    print (URL)
    response = requests.get(URL)
    return response.json()
    

def main():
    print ("\nWhat up homie. Enter your region to get started")
    print ("Type in one of the following regions or else the program wont work correctly:\n")
    print ("NA or EUW (Note: You can add more regions by just changing up the URL!\n")

    #I first ask the user for three things, their region, summoner name, and API Key.
    #These are the only three things I need from them in order to get create my URL and grab their ID.

    region = (str)(input('Type in one of the regions above: '))
    summonerName = (str)(input('Type your Summoner Name here and DO NOT INCLUDE ANY SPACES: '))
    APIKey = "RGAPI-5642669a-b1c7-49f2-a5ee-3655df1f5663"

    #I send these three pieces off to my requestData function which will create the URL and give me back a JSON that has the ID for that specific summoner.
    #Once again, what requestData returns is a JSON.
    responseJSON  = requestSummonerData(region, summonerName, APIKey)
    
    ID = responseJSON[summonerName]['id']
    ID = str(ID)
    print (ID)
    responseJSON2 = requestRankedData(region, ID, APIKey)
    print (responseJSON2[ID][0]['tier'])
    print (responseJSON2[ID][0]['entries'][0]['division'])
    print (responseJSON2[ID][0]['entries'][0]['leaguePoints'])

#This starts my program!
if __name__ == "__main__":
    main()
