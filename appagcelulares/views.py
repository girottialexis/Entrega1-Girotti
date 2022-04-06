from ast import Return
from django.shortcuts import render
from django.http import HttpResponse
from appagcelulares.models import Cliente, Equipo, Fichatecnica, Familiar
from appagcelulares.forms import Clienteformulario, Equipoformulario, Fichatecnicaformulario, Familiarformulario


# Create your views here.

def pagina_inicio(request):
    return render(request, "appagcelulares/inicio.html")

def clientes(request):
        cliente = Cliente.objects.all()

        if request.method == "POST":

            cliente = Clienteformulario(request.POST)
            print(cliente)

            if cliente.is_valid():
                data =  cliente.cleaned_data

                cliente_nuevo = Cliente(data['nombre'], data['apellido'], data['dni'])
                cliente_nuevo.save()

            cliente_form = Clienteformulario()
            return render(request, "appagcelulares/clientes.html", {"formulario": cliente_form })

        else:
            
           
            cliente_form = Clienteformulario()
            return render(request, "appagcelulares/clientes.html", {"formulario": cliente_form })

def equipos(request):
        equipo = Equipo.objects.all()

        if request.method == "POST":

            equipo = Equipoformulario(request.POST)
            print(equipo)

            if equipo.is_valid():
                data =  equipo.cleaned_data

                equipo_nuevo = Equipo(data['modelo_equipo'], data['numero_telefono'])
                equipo_nuevo.save()

            equipo_form = Equipoformulario()
            return render(request, "appagcelulares/equipos.html", {"formulario":equipo_form})
        else:
            
           
            equipo_form = Equipoformulario()
            return render(request, "appagcelulares/equipos.html", {"formulario":equipo_form})


def fichastecnicas(request):
        ficha = Fichatecnica.objects.all()

        if request.method == "POST":

            ficha = Fichatecnicaformulario(request.POST)
            print(ficha)

            if ficha.is_valid():
                data =  ficha.cleaned_data

                ficha_nueva = Fichatecnica(data['numero_ficha'], data['fecha_recibido'], data['problema_tecnico'], data['reparado'], data['fecha_entregado'])
                ficha_nueva.save()

            ficha_form = Fichatecnicaformulario()
            return render(request, "appagcelulares/fichastecnicas.html", {"formulario":ficha_form})
        else:
            
           
            ficha_form = Fichatecnicaformulario()
            return render(request, "appagcelulares/fichastecnicas.html", {"formulario":ficha_form})

def buscarclientes(request):
    
    data = request.GET.get("dni")
    
    print(data)

    if data:
        cliente = Cliente.objects.filter(dni__icontains = data)

        return render(request, "appagcelulares/buscarcliente.html", {"cliente": cliente[0]})
    
    return render(request, "appagcelulares/buscarcliente.html")


def plantilla(request):
    
    return render(request, "appagcelulares/plantilla.html")


def familiar(request):
         
         familiar = Familiar.objects.all()

         if request.method == "POST":

             familiar = Familiarformulario(request.POST)
             print(familiar)

             if familiar.is_valid():
                 data =  familiar.cleaned_data

                 familiar_nuevo = Familiar(data['nombre'], data['apellido'], data['dni'], data['fecha_nac'])
                 familiar_nuevo.save()

             familiar_form = Familiarformulario()
             return render(request, "appagcelulares/familiar.html", {"formulario": familiar_form, "familiar": familiar})

         else:
            
           
             familiar_form = Familiarformulario()
             return render(request, "appagcelulares/familiar.html", {"formulario": familiar_form })
