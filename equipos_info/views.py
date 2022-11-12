from django.shortcuts import render
from NBA_stats.models import Equipo
from django.contrib.auth.decorators import login_required


#@login_required
def equipos_info(request):
    teams = Equipo.objects.order_by('nombre')
    context = {'equipos' : teams}

    return render(request, 'equipos_info/equipos_info.html')