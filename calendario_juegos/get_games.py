import requests
from calendario_juegos.juegos import Juego
from datetime import date

URL = "https://api-nba-v1.p.rapidapi.com/games"

HEADERS = {
	"X-RapidAPI-Key": "c1d97fa4dbmshd7217d7e021e446p147efcjsn6097dc6a513a",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}


def get_games (querystring={"date": date.today()}):

	response = requests.request("GET", URL, headers=HEADERS, params=querystring)

	response_json: dict = response.json()

	juegos = response_json["response"]

	lista_juegos = []

	for juego in juegos:

		fecha = juego["date"]
		estado = juego["status"]
		equipos = juego["teams"]
		scores = juego["scores"]

		a: Juego = Juego(fecha, estado, equipos, scores)

		lista_juegos.append(a)

	return lista_juegos

