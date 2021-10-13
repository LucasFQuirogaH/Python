"""------------------------------------------------------------------------------------------------------------
M O D U R A M A             E S T O S   S O N   M I S   M O D U L O S           M O D U R A M A
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""

# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Parse CSV ---------------------------------------------------------------------------------------
# %%
import csv
def parse_csv(lines , select = None , types = None , has_headers = True , silence_errors = False):
#Parsea un archivo CSV en una lista de registros con conversión de tipos.
    import csv
    if select and not has_headers:
        raise RuntimeError('para seleccionar columnas, el archivo tiene que tener encabezado')
    rows = csv.reader(lines)
    # Leer los encabezados (si hubiera)
    headers = next(rows) if has_headers else []
    # Si se seleccionaron columnas, generar sus índices
    if select:
        indices = [ headers.index(col) for col in select ]
        headers = select
    registros = []
    for i, row in enumerate(rows, 1):
        if not row:     # Saltear filas vacías
            continue
        # Si se seleccionaron columnas, tomar de la fila esos datos
        if select:
            row = [ row[index] for index in indices]
        # Convertir los tipos de la fila
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Fila {i}: No pude convertir {row}")
                    print(f"Fila {i}: Motivo {e}")
                continue
        # Hacer un diccionario o una tupla
        if headers:
            registro = dict(zip(headers, row))
        else:
            registro = tuple(row)
        registros.append(registro)
    return registros

## Funciones: Leer Camion -------------------------------------------------------------------------------------
# %%
def leer_camion(nom_archivo):
# Lee un archivo de lotes en un camión
# y lo devuelve como lista de diccionarios con claves
# nombre, cajones, precio.
    Nombre = "C:\Python/Unsam Python/Data/" + nom_archivo + ".csv"
    with open(Nombre) as file:
        camiondicts = parse_csv(file , select=['nombre','cajones','precio'] , types=[str,int,float])
    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts]
    return Camion(camion)
## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def filematch(filename, substr):
#Contrato: Se le entrega una direccion y una palabra a buscar y devuelve la linea donde esta esa palabra.
# Ambos parametrsi entre comillas.
# Precondicion: Entre comillas, una direccion completa en el disco y una palabra o frase
# Poscondicion:
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line

# Clases -----------------------------------------------------------------------------------------------------
# %%
# Clase Lote
class Lote:
    def __init__(self, nombre, cajones , precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    def __repr__(self):
        return f'Lote({self.nombre} , {self.cajones} , {self.precio})'
    def __str__(self):
        return f'({self.nombre},{self.cajones},{self.precio})'
    def costo(self):
        costo = self.precio * self.cajones
        return (costo)
    def vender(self , cantidad):
        total = self.precio * cantidad
        return (total)

class Camion:
    def __init__(self, lotes):
        self.lotes = lotes
    def __iter__(self):
        return self.lotes.__iter__()
    def __len__(self):
        return len(self.lotes)
    def __getitem__(self, index):
        return self.lotes[index]
    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])
    def precio_total(self):
        return sum([l.costo() for l in self.lotes])

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total