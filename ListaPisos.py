from lista import listaPatron, celdita
from nodo import nodoSimple

class pisoss: 
    def __init__(self, nombre, filas, columnas, flipe, slide):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.flipe = flipe
        self.slide = slide
        self.patron = listaPatron()
        self.celdas = celdita()

class listaSimple:
    def __init__(self):
        self.primero = None
    
    def insertarLP(self, piso):
        if self.primero is None:
            self.primero = nodoSimple(pisos=piso)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodoSimple(pisos=piso)

    def mostrar(self):
        actual = self.primero
        while actual != None:
            #print("Nombre", actual.pisos.nombre, "Fila: ", actual.pisos.filas, "Columna: ", actual.pisos.columnas, "Flipe: ", actual.pisos.flipe, "Slide: ", actual.pisos.slide)
            actual = actual.siguiente
        