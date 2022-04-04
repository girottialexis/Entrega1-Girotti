from multiprocessing.connection import Client
from django.contrib import admin
from appagcelulares.models import Cliente, Equipo, Fichatecnica, Familiar

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Equipo)
admin.site.register(Fichatecnica)
admin.site.register(Familiar)