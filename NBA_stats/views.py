from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime
from NBA_stats.models import Equipo
from NBA_stats.get_team_stats import get_stats


#@login_required
def home(request):
    equipos = Equipo.objects.order_by('nombre')
    context = {'equipos' : equipos, 'id_equipo_1' : 0, 'id_equipo_2' : 40}
    return render(request, 'NBA_stats/home.html', context)


#@login_required
def team_vs_team(request):
    home = request.GET["home"]
    visitor = request.GET["visitor"]
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    
    home_img = "/static/images/logos/imagen_equipo_" + home + ".png"
    visitor_img = "/static/images/logos/imagen_equipo_" + visitor + ".png"


    # Obtener estadisticas de equipo
    #home_stats = get_stats({"id":home, "season":year})
    #visitor_stats = get_stats({"id":visitor, "season":year})

    #context = {"home_img": home_img, "visitor_img": visitor_img, "home_stats": home_stats, "visitor_stats", visitor_stats}
    context={"home_img": home_img, "visitor_img": visitor_img}
    return render(request, 'NBA_stats/TeamVsTeam.html', context)


def cerrar_sesion(request):
    logout(request)
    return redirect('/')
