# formato_tabla.py

class FormatoTabla:
    def encabezado(self, headers):
        raise NotImplementedError()

    def fila(self, rowdata):
        raise NotImplementedError()

class FormatoTablaTXT(FormatoTabla):
# Generar una tabla en formato TXT
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

class FormatoTablaCSV(FormatoTabla):
# Generar una tabla en formato CSV
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))


class FormatoTablaHTML(FormatoTabla):
# Generar una tabla en formato HTML
    def encabezado(self, headers):
        print("<tr><th>" + headers[0] + "</th><th>" + headers[1] + "</th><th>" + headers[2] + "</th><th>" + headers[3] + "</th></tr>")

    def fila(self, data_fila):
        print("<tr><td>" + data_fila[0] + "</td><td>" + data_fila[1] + "</td><td>" + data_fila[2] + "</td><td>" + data_fila[3] + "</td></tr>")
#--------------------------------------------------------------------
# %%
# El Formateador
def crear_formateador(nombre):
    if nombre == "txt":
        return FormatoTablaTXT()
    elif nombre == "csv":
        return FormatoTablaCSV()
    elif nombre == "html":
        return FormatoTablaHTML()
    else:
        raise SystemExit ("No se entiende el formato")
    #--------------------------------------------------------------------
# %%
# Imprimir tabla
def imprimir_tabla(Camion , Columnas , formateador):
    UnaLista = []
    # Llamo al formateador y formateo las columnas
    formateador.encabezado(Columnas)
    for Fila in Camion:
        UnaLista = []
        for Columna in Columnas:
            # Tomas en la Fila, solo el atributo que se corresponda con la columna
            UnaLista.append(str(getattr(Fila , Columna)))
        formateador.fila(UnaLista)
    return None
