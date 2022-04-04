from unicodedata import name
from django.urls import path
from appagcelulares.views import *

urlpatterns = [
    path('', pagina_inicio, name= "Inicio"),
    path('clientes/', clientes, name="Clientes"),
    path('equipos/', equipos, name="Equipos" ),
    path('fichastecnicas/', fichastecnicas, name="Fichastecnicas" ),
    path('clientessearch/', buscarclientes, name="Buscarclientes" ),
    path('familiar/', familiar, name="Familiar" ),
]
