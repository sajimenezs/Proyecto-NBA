import requests
from NBA_stats.team_stats import Team_stats


URL = "https://api-nba-v1.p.rapidapi.com/teams/statistics"

HEADERS = {
	"X-RapidAPI-Key": "c1d97fa4dbmshd7217d7e021e446p147efcjsn6097dc6a513a",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}


def get_stats (querystring):

	response = requests.request("GET", URL, headers=HEADERS, params=querystring)

	response_json: dict = response.json()

	stats_equipo = response_json["response"]

	a = Team_stats(stats_equipo[0])

	return a