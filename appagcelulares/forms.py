from django import forms


class Clienteformulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()


class Equipoformulario(forms.Form):

    modelo_equipo = forms.CharField(max_length=40)
    numero_telefono = forms.IntegerField()

class Fichatecnicaformulario(forms.Form):

    numero_ficha = forms.IntegerField()
    fecha_recibido = forms.DateField()
    problema_tecnico = forms.CharField(max_length=300)
    reparado = forms.BooleanField()
    fecha_entregado = forms.DateField()

