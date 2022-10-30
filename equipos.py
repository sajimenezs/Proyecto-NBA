import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NBA_project.settings')
django.setup()

from NBA_stats.models import Equipo


a = Equipo(
    id_equipo=1,
    nombre="Atlanta Hawks",
    apodo="Hawks",
    codigo="ATL",
    ciudad="Atlanta",
    escudo="Hawks_2016.png",
)

a.save()