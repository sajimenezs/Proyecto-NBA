def plantilla_equipo(self):

 url = "https://api-nba-v1.p.rapidapi.com/players"

 headers = {
	"X-RapidAPI-Key": "c1d97fa4dbmshd7217d7e021e446p147efcjsn6097dc6a513a",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

 response = requests.request("GET", url, headers=headers)
 response_json: dict = response.json()
 players = response_json["response"]

 m=17 ##Máximo número de jugadores en un equipo


 for player in players:
   if(player["team"]["name"]==self.name):
     team_players=team_players.append(player["name"])

 #Crea el listado de jugadores del equipo

 return team_players
