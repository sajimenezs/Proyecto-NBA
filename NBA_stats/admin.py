from django.contrib import admin
from .models import Equipo


class EquipoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'id_equipo', 'ciudad')

    search_fields = ('nombre', 'id_equipo', 'ciudad')

    ordering = ('id_equipo',)


admin.site.register(Equipo, EquipoAdmin)
