import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NBA_project.settings')
django.setup()

from NBA_stats.models import Equipo

import requests

url = "https://api-nba-v1.p.rapidapi.com/teams"

headers = {
	"X-RapidAPI-Key": "c1d97fa4dbmshd7217d7e021e446p147efcjsn6097dc6a513a",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

response_json: dict = response.json()
equipos = response_json["response"]
n = 41 # Limite equipos NBA (40)

id_equipo = [equipos[i]["id"] for i in range(n)]
nombre = [equipos[i]["name"] for i in range(n)]
apodo = [equipos[i]["nickname"] for i in range(n)]
codigo = [equipos[i]["code"] for i in range(n)]
ciudad = [equipos[i]["city"] for i in range(n)]


for i in range(n):

    a = Equipo(
        id_equipo=(id_equipo[i] - 1),
        nombre=nombre[i],
        apodo=apodo[i],
        codigo=codigo[i],
        ciudad=ciudad[i],
        escudo="imagen_equipo_" + str(i) + ".png",
    )

    a.save()