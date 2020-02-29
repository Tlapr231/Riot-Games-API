import requests

APIKey = "RGAPI-7a3af3d3-56fa-46af-8a8d-a3008e264e93" #Expires: Fri, Jul 5th, 2019 @ 1:15pm (PT)
RegionKey = {'BR' : 'br1' , 'EUNE' : 'eun1', 'EUW' : 'euw1', 'JP' : 'jp1' , 'KR' : 'kr' , 'LAN' : 'la1', 'LAS' : 'la2', 'NA' : 'na1', 'OCE' : 'oc1' , 'TR' : 'tr1', 'RU' : 'ru', 'PBE' : 'pbe1'}

def getSumInfo(region, name) :

    Url = "https://" + RegionKey[region.strip().upper()] + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name.strip() + "?api_key=" + APIKey
    #print(Url)

    response = requests.get(Url)

    return response.json()


def getSumRank(region, id) :

    Url = "https://" + RegionKey[region.strip().upper()] + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + id + "?api_key=" + APIKey
    #print(Url)

    response = requests.get(Url)

    return response.json()


def getSumLiveGame(region, id) :

    Url = "https://" + RegionKey[region.strip().upper()] + ".api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + id + "?api_key=" + APIKey
    #print(Url)

    return True



Region = str(input("Region : "))
SummonerName = str(input("Summoner Name : "))

Summonerdata = getSumInfo(Region, SummonerName)

RankData = getSumRank(Region, Summonerdata['id'])

GameData = getSumLiveGame(Region, Summonerdata['id'])

Data = RankData[0]

# print("Name : " + Summonerdata['name'])
# print("Name : " + Data['summonerName'])
# print("Tier : " + Data['tier'])
# print("Rank : " + Data['rank'])
# print("LP : " + str(Data['leaguePoints']))
# print("Wins : " + str(Data['wins']))
# print("Losses : "+ str(Data['losses']))

string = str(Data['summonerName']) + " is curently " + str(Data['tier']) + " " + str(Data['rank']) + " with " + str(Data['leaguePoints']) + " lp and a winrate of " + str(round(Data['wins']*100/(Data['wins'] + Data['losses']),1)) + "%."
print(string)
