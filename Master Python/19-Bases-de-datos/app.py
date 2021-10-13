"""------------------------------------------------------------------------------------------------------------
Costo Camion modificado para importar modulos.
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# %%
# Import ------------------------------------------------------------------------------------------------------
import sqlite3
from pprint import pprint
import os
# Funcions ----------------------------------------------------------------------------------------------------
## Funcions: Show All -----------------------------------------------------------------------------------------
# %%
def ShowAll():
    """Contrat: Show a full table
    Precondition:
    Poscondition:"""
    conexion = sqlite3.connect('customer.db')
    print((conexion.execute("selec rowid, * from Clientes")).fetchall())
    conexion.commit()
    conexion.close()
    return None
## Funcions: Busqueda lineal ----------------------------------------------------------------------------------
# %%
def AddRow(Nombre, Apellido , Email):
    """Contrat: Add a row
    Precondicion:
    Poscondicion:"""
    conexion = sqlite3.connect('customer.db')
    conexion.execute('Insert into Clientes (Nombre , Apellido , Email) Values (? , ? , ?)' , (Nombre , Apellido , Email))
    conexion.commit()
    conexion.close()
    return None
## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def AddMultipleRows(list):
    #--------------------------------------------------------------------
    """Contrat: the list must be composed of tuples separated by commas.
    Each tuple must contain the same number of fields as the table.
    Poscondicion:"""
    conexion = sqlite3.connect('customer.db')
    conexion.executemany("Insert into Clientes values (? , ? , ?)" , list)
    conexion.commit()
    conexion.close()
    return None
## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def CreateTable():
    """Contrat: Create a table with field of Name, Surname and Email.
    Precondicion:
    Poscondicion:"""
    conexion = sqlite3.connect('customer.db')
    try:
        conexion.execute(""" Create table Clientes(
                        Nombre text,
                        Apellido text,
                        Email text
                    )""")
    except sqlite3.OperationalError:
        print('Ya existe')
    conexion.commit()
    conexion.close()
    return None

























## Funcions: Main Funtion  ------------------------------------------------------------------------------------
# %%
def main():
# El main como programa principal
    os.chdir('C:\\Python/SQL/SQLite Full Course')
    return None

# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()