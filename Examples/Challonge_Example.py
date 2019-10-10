import requests
import Credentials
import json

challongeKey = Credentials.get_challongeKey();
challongeURL = "https://api.challonge.com/v1/"

parameters = {
    "api_key": challongeKey,
    "tournament": "Mika71618b"
}

response = requests.get(challongeURL + "tournaments.json", params=parameters)

print(response.status_code)

parameters = {
    "api_key": challongeKey,
    "tournament": "Mika71618b"
}

participants = requests.get(challongeURL + "/tournaments/Mika71618b/participants.json", params=parameters)
values = json.loads(participants.text)

print(participants.status_code)

#Print the name of all participants for a given tournament
for index in range(len(values)):
    print(values[index]['participant']['name'])