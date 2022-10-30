from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from NBA_stats.models import Equipo


@login_required
def home(request):
    equipos = Equipo.objects.order_by('nombre')
    return render(request, 'NBA_stats/home.html', {'equipos' : equipos})


def cerrar_sesion(request):
    logout(request)
    return redirect('/')
