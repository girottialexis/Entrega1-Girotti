from ast import Return
from django.shortcuts import render
from django.http import HttpResponse
from appagcelulares.models import Cliente
from appagcelulares.forms import Clienteformulario


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
    return render(request, "appagcelulares/equipos.html")

def fichastecnicas(request):
    return render(request, "appagcelulares/fichastecnicas.html")

def buscarclientes(request):
    
    data = request.GET.get("dni")
    
    print(data)

    if data:
        cliente = Cliente.objects.filter(dni__icontains = data)

        return render(request, "appagcelulares/buscarcliente.html", {"cliente": cliente[0]})
    
    return render(request, "appagcelulares/buscarcliente.html")