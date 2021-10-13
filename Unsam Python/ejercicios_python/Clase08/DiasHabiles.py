"""------------------------------------------------------------------------------------------------------------
Ejercicio 8.4: Días hábiles
Escribí una función dias_habiles(inicio, fin, feriados) que calcule los días hábiles entre dos fechas dadas.
La función debe tener como argumentos el día inicial, el día final, y una lista con las fechas correspondientes
a los feriados que haya en ese lapso, y debe devolver una lista con las fechas de días hábiles del período,
incluyendo la fecha inicial y la fecha final indicadas. Las fechas de entrada y salida deben manejarse
en formato de texto.
Consideramos día hábil a un día que no es feriado ni sábado ni domingo.

Probala entre el 20 de septiembre de 2020 y el 10 de octubre del mismo año, sabiendo que no hubo feriados
en el medio. Probala entre ese día y fin del 2020 considerando los siguientes feriados de Argentina:
feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']

Ing.Lucas F. Quiroga H. Fecha: 07/05/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%
from datetime import datetime, date , timedelta
import copy
import pprint

# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Dias Habiles ------------------------------------------------------------------------------------
# %%
def dias_habiles(inicio, fin, feriados):
#Contrato: La funcion tiene asignados 3 parametros. 2 fechas, una de inicio y otra de fin. Y una lista con los
# feriados a comparar. Ambos paramatros deben estar en formato dd/mm/aaaa.
# Precondicion: 2 Fechas en formato dd/mm/aaaa, en formato string, y una lista con el mismo formato.
# Poscondicion: La funcion devuelve una lista con las fechas que cumplen la condicion de ser dias habiles,
# es decir: dias de lunes a viernes y que no se encuentren en la lista de los feriados suministrados
# por el operador.
    FormatoFeriados = []

    #Formateo de la fecha de inicio
    FechaDeInicioSplitteada = inicio.split("/")
    FormatoInicio = date(int(FechaDeInicioSplitteada[2]) , int(FechaDeInicioSplitteada[1]) , int(FechaDeInicioSplitteada[0]))

    #Formateo de la fecha del fin
    FechaFinSplitteada = fin.split("/")
    FormatoFin = date(int(FechaFinSplitteada[2]) , int(FechaFinSplitteada[1]) , int(FechaFinSplitteada[0]))

    #Formateo de la fecha de los feriados
    for Fecha in feriados:
        FechaFeriadosSplitteada = Fecha.split("/")
        FormatoFeriados.append(str(date(int(FechaFeriadosSplitteada[2]) , int(FechaFeriadosSplitteada[1]) , int(FechaFeriadosSplitteada[0]))))

    # Definicion de variables antes del while
    InicioIncremental = copy.deepcopy(FormatoInicio)
    UnDia = timedelta(days = 1)
    ListaDeDias = []

    # Solo por si cae en sabado o domingo
    if InicioIncremental.weekday() == 5: # Sabado
        InicioIncremental = InicioIncremental + UnDia + UnDia
    elif InicioIncremental.weekday() == 6: # Domingo
        InicioIncremental = InicioIncremental + UnDia

    # Iterador =)
    while(InicioIncremental != FormatoFin):
        InicioIncremental += UnDia
        if (InicioIncremental.weekday() < 5) and (str(InicioIncremental) not in FormatoFeriados):
            ListaDeDias.append(str(InicioIncremental))

    return ListaDeDias

## Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main():
# El main como programa principal
    FechaDeInicio = "20/09/2020"
    FechaFin = "31/12/2020"
    Feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']
    pprint.pprint(dias_habiles(FechaDeInicio , FechaFin , Feriados))
    return None

# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()

