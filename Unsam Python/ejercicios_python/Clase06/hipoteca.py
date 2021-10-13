"""--------------------------------------------------------------------------------------------------------------------
SE LE PIDE AL OPERADOR QUE COMENTE O DESCOMENTE LA PARTE DEL CODIGO QUE VA A EVALUAR EN EL MOMENTO QUE LO PRECISE.
TODOS LOS EJERCICIOS SE ENCUENTRAN FUNCIONANDO.
SALUDOS. LUCAS QUIROGA.
--------------------------------------------------------------------------------------------------------------------"""








"""--------------------------------------------------------------------------------------------------------------------
Ejercicio 1.7: La hipoteca de David
David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%.
Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.

El siguiente es un programa que calcula el monto total que pagará David a lo largo de los años:
--------------------------------------------------------------------------------------------------------------------"""

# Main principal ----------------------------------------------------------------------------------------------------------
# hipoteca.py suministrado por los profesores/as

# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0

# while saldo > 0:
#     saldo = saldo * (1+tasa/12) - pago_mensual
#     total_pagado = total_pagado + pago_mensual

# print('Total pagado', round(total_pagado, 2))

"""--------------------------------------------------------------------------------------------------------------------
Ejercicio 1.8: Adelantos
Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.

Modificá el programa para incorporar estos pagos extra y que imprima el monto total pagado junto con la
cantidad de meses requeridos.

Cuando lo corras, este nuevo programa debería dar un pago total de 929965.62 en 342 meses.

Aclaración: aunque puede parecer sencillo, este ejercicio requiere que agregues una variable mes y
que prestes bastante atención a cuándo la incrementás, con qué valor entra al ciclo y con qué valor sale del ciclo.
Una posiblidad es inicializar mes en 0 y otra es inicializarla en 1.
En el primer caso es problable que la variable salga del ciclo contando la cantidad de pagos que se hicieron,
en el segundo, ¡es probable que salga contando la cantidad de pagos más uno!
--------------------------------------------------------------------------------------------------------------------"""

#Main modificado para adelantos---------------------------------------------------------------------------------------------

# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# meses_acumulados = 0

# for i in range (12): #-------------------------------------------Colocamos los 1000 pesos extra, los primeros 12 meses
#     if saldo > 0:
#         saldo = saldo * (1+tasa/12) - pago_mensual - 1000
#         total_pagado = total_pagado + pago_mensual + 1000
#         meses_acumulados +=1
# #------------------------------------------------------------------------------------------Fin de los primeros 12 meses
# while saldo > 0:
#     saldo = saldo * (1+tasa/12) - pago_mensual
#     total_pagado = total_pagado + pago_mensual
#     meses_acumulados +=1

# print('Total pagado', round(total_pagado, 2))
# print(f"\nTotal pagado: {round(total_pagado, 2)}")
# print(f"\nCantidad de meses: {meses_acumulados}")

"""--------------------------------------------------------------------------------------------------------------------
Ejercicio 1.9: Calculadora de adelantos
¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, comenzando en el sexto año de la hipoteca
(es decir, luego de 5 años)?

Modificá tu programa de forma que la información sobre pagos extras sea incorporada de manera versátil.
Agregá las siguientes variables antes del ciclo, para definir el comienzo, fin y monto de los pagos extras:
--------------------------------------------------------------------------------------------------------------------"""

#Main modificado para calculadora de adelantos---------------------------------------------------------------------------

# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# meses_acumulados = 0
# pago_extra = 1000
# pago_extra_mes_comienzo = 61
# pago_extra_mes_fin = 108
   
# while saldo > 0:
#     if ((meses_acumulados < pago_extra_mes_comienzo) or (meses_acumulados > pago_extra_mes_fin)):
#         saldo = saldo * (1+tasa/12) - pago_mensual
#         total_pagado = total_pagado + pago_mensual
#     else:
#         saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
#         total_pagado = total_pagado + pago_mensual + pago_extra

#     meses_acumulados +=1

# print(f"\nTotal pagado: {round(total_pagado, 2)}")
# print(f"\nCantidad de meses: {meses_acumulados}")


"""--------------------------------------------------------------------------------------------------------------------
Ejercicio 1.10: Tablas
Modicá tu programa para que imprima una tabla mostrando el mes, el total pagado hasta el momento y el saldo restante.
--------------------------------------------------------------------------------------------------------------------"""

#Main modificado para Tablas------------------------------------------------------------------------------------------

# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# meses_acumulados = 0
# pago_extra = 1000
# pago_extra_mes_comienzo = 61
# pago_extra_mes_fin = 108

# print("Mes\tTotal Pagado\tSaldo Restante")   
# while saldo > 0:
#     if ((meses_acumulados < pago_extra_mes_comienzo) or (meses_acumulados > pago_extra_mes_fin)):
#         saldo = saldo * (1+tasa/12) - pago_mensual
#         total_pagado = total_pagado + pago_mensual
#     else:
#         saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
#         total_pagado = total_pagado + pago_mensual + pago_extra
#     meses_acumulados +=1
#     print(f"{meses_acumulados} \t{round(total_pagado, 2)} \t{round(saldo, 2)}")
     
"""--------------------------------------------------------------------------------------------------------------------
Ejercicio 1.11: Bonus
Ya que estamos, corregí el código anterior de forma que el pago del último mes se ajuste a lo adeudado.

Asegurate de guardar en el archivo hipoteca.py
esta última versión en tu directorio ejercicios_python/Clase01/. Vamos a volver a trabajar con él.
--------------------------------------------------------------------------------------------------------------------"""

# Main modificado para calcular la ultima cuota con saldo ajustado----------------------------------------------------------

# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# meses_acumulados = 0
# pago_extra = 1000
# pago_extra_mes_comienzo = 61
# pago_extra_mes_fin = 108

# print("Mes\tTotal Pagado\tSaldo Restante")   
# while saldo > 0:
#     if saldo >= pago_mensual: #--------------------------------------------Pregunta si el saldo es mayor a un pago mensual.
#         if ((meses_acumulados < pago_extra_mes_comienzo) or (meses_acumulados > pago_extra_mes_fin)):
#             saldo = saldo * (1+tasa/12) - pago_mensual
#             total_pagado = total_pagado + pago_mensual
#         else:
#             saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
#             total_pagado = total_pagado + pago_mensual + pago_extra
#     else:#--------------------En la ultima cuota podria quedar un monto inferior al pago mensual, entonces pagaria menos.
#         total_pagado = total_pagado + saldo
#         saldo = 0
#     meses_acumulados +=1
#     print(f"{meses_acumulados} \t{round(total_pagado, 2)} \t{round(saldo, 2)}")
# print("\nMonto cancelado")