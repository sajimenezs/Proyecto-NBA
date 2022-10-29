from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def home(request):
    return render(request, 'NBA_stats/home.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('/')
