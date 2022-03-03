from django.http import HttpResponse
import datetime

def saludo(request):
    silaba = """
    <html>
    <body>
    <h1>
    Hola alumnos esta es nuestra primera vista
    <h1/>
    <body/>
    <html/>
    """
    return HttpResponse(silaba)

def despedida(request):
    return HttpResponse("hasta luego")

#--------------------------------------------------------------------
def dameFecha(Request):
    fecha_actual = datetime.datetime.now()
    Hora = """
    <html>
    <body>
    <h1>
    Hora y fecha actuales %s
    <h1/>
    <body/>
    <html/>
    """ %fecha_actual
    return HttpResponse(Hora)

#--------------------------------------------------------------------
def calculaEdad(request , anio): # Aqui le pasas un solo parametro
    edadActual = 40
    periodo = anio - 2022
    edadFutura = edadActual + periodo
    docHTML = """
    <html>
    <body>
    <h1>
    En el año %s tendras %s años
    <h1/>
    <section>
    <h2>
    <h2/>
    <section/>
    <body/>
    <html/>
    """ %(anio ,edadFutura)
    return (HttpResponse(docHTML))
#--------------------------------------------------------------------

def calculaEdad2(request , edad , anio): # Aqui le pasas 2 parametros
    #edadActual = 40
    periodo = anio - 2022
    edadFutura = edad + periodo
    doc2HTML = """
    <html>
    <body>
    <h1>
    En el año %s tendras %s años
    <h1/>
    <section>
    <h2>
    <h2/>
    <section/>
    <body/>
    <html/>
    """ %(anio ,edadFutura)
    return (HttpResponse(doc2HTML))
#--------------------------------------------------------------------