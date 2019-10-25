#Accepts a Challonge Link and populates the database based on information
import requests
import Credentials
import json

challongeKey = Credentials.get_challongeKey();
challongeURL = "https://api.challonge.com/v1/"

#Retrieves all the participants given a tournament URl
def getParticipants(tournament):
    parameters = {
        "api_key": challongeKey,
        "tournament": tournament
    }
    participants = requests.get(challongeURL + "/tournaments/" + tournament + "/participants.json", params=parameters)
    values = json.loads(participants.text)
    dict = []
    for i in range(len(values)):
        dict.append(values[i]['participant']['name'])

    return dict

#Takes a tag and returns it with special characters removed
def reformatTag(tag):
    bad_characters = ["?", "!"]
    for i in bad_characters:
        tag = tag.replace(i, "")
    return tag

#Retrieves all of the challonge tournaments for a given user
def getTournaments(user):
    #"https://Mikazuchi:", challonge_key, "@api.challonge.com/v1/"
    parameters = {
        "api_key": challongeKey,
        "state": "all",
        "type": "double elimination",
        "created_after": "2017-01-01",
        "created_before": "2019-12-31"
    }

    participants = requests.get("https://" + user + ":" + challongeKey + "@api.challonge.com/v1/tournaments.json", params=parameters)
    #print(participants.status_code)
    values = json.loads(participants.text)
    return values

#Retrieves all of the Tournament info
def getTourneyInfo(tournament):
    parameters = {
        "api_key": challongeKey,
    }
    tourneyInfo = requests.get(challongeURL + "/tournaments/" + tournament + ".json", params=parameters)
    values = json.loads(tourneyInfo.text)
    return values

#Returns the date a tournament occured on in the format of __-
def getDate(tournament):
    date = getTourneyInfo(tournament)['tournament']['created_at']
    return date

def getMatches(tournament):
    parameters = {
        "api_key": challongeKey,
    }

    matches = requests.get(challongeURL + "/tournaments/" + tournament + "/matches.json", params=parameters)
    values = json.loads(matches.text)
    return values

#print(getParticipants("Mika71618b"))
#print(getTournaments("Mikazuchi"))
#print(getTourneyInfo("Mika71618b"))
#print(getDate("Mika71618B"))
#print(getMatches("Mika71618B"))
