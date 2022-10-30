from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def calendario_juegos(request):
    return render(request, 'calendario_juegos/calendario.html')
