# AG Celulares
## _Proyecto CODER_

Contenido del programa:

- Información General 
- Estructura  
- Instalación 
- Funcionamiento
- Tecnologías 


## Información General

El siguiente programa esta pensado para un uso similar a un software de una compañia de arreglo de celulares tanto para gestión de cliente como el seguimiento de órdenes de reparación de equipos.

## Estructura

El programa se esquematiza de la siguiente manera:

- /appagcelulares/ (pagina inicio)
- /appagcelulares/clientes/ (pagina clientes)
- /appagcelulares/equipos/ (pagina equipos)
- /appagcelulares/fichastecnicas/ (pagina fichas tecnicas)
- /appagcelulares/clientessearch/ (pagina buscar clientes)

## Instalación

Para la instalación deberán seguirse los siguientes pasos:

```sh
1.Debes clonar el proyecto desde el siguiente LINK:
git clone: https://github.com/girottialexis/Entrega1-Girotti.git
2.Contar con la instalacion de Python y Django
3.Desde la terminal abrir la carpeta Entrega1-Girotti
4.Correr el servidor: python manage.py runserver
5.Abrir la pagina desde http://127.0.0.1:8000/
6.Ya puedes navegar en la web.
```

## Funcionamiento

Una vez ejecutado el servidor, accediendo a la pagina de inicio tenemos las secciones de clientes, equipos y fichas tecnicas.
Cada una de ellas contendrá la posibilidad de agregar clientes a la base de datos como asi también observar el listado de elementos que la componen.
En esta primer versión solo se encuentra disponible el esquema de carga de datos unicamente para clientes. Ingresando en dicha sección e incorporando los datos podemos dar de alta a cualquier persona. También para estos elementos tenemos un buscador a través de la ejecución /clientessearch/ que funciona a través del DNI del cliente.

## Tecnologías
Necesitaras contar con los siguientes programas instalados:

```sh
1.Python 3.7
2.Django 9.6
```
