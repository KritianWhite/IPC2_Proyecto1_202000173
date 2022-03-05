from tkinter import Label
from tkinter.constants import ACTIVE, TRUE

from matplotlib.pyplot import get
from nodo import Nodo
from graphviz import Digraph, Graph


class lista:
    def __init__(self):
        #self.cabecera : Nodo = None
        self.cabecera = None

    '''
    def Agregar(self, x):
        nuevoNodo = Nodo(x)
        #print('Kheee')
        if self.cabecera != None:
            self.cabecera = nuevoNodo
        else:
            auxiliarNodo = self.cabecera
            while auxiliarNodo.siguiete is not None:
                auxiliarNodo = auxiliarNodo.siguiete
            auxiliarNodo.siguiete = nuevoNodo
    
    def impresion(self):
        auxNodo = self.cabecera
        while auxNodo is not None:
            print(auxNodo.x)
            auxNodo = auxNodo.siguiete
    '''

    def Colocar(self, xx):
        temp = Nodo(xx)
        temp.setSiguiente(self.cabecera)
        self.cabecera = temp

    def Agregar(self, xx):
        if not self.cabecera:
            self.cabecera = Nodo(xx)
            return
        correrPiso = self.cabecera
        while correrPiso.siguiete:
            correrPiso = correrPiso.siguiete
        correrPiso.siguiete = Nodo(xx)
     
    def tamanio(self):
        actual = self.cabecera
        contador = 0
        if actual != None:
            while actual != None:
                contador += 1
                actual = actual.getSiguiente()
                
        return contador

    def Eliminar(self, xx):
        actual = self.cabecera
        antes = None
        localizado = False
        while not localizado:
            if actual.getPatron() == xx:
                localizado = True
            else:
                antes = actual
                actual = actual.getSiguiente()
        if antes == None:
            self.cabecera = actual.getSiguiente()
        else:
            antes.setSiguiente(actual.getSiguiente())

    def imprimirCelda(self):
        actual = self.cabecera
        text = ''
        while actual != None:
            text += '|'
            text += str(actual.getPatron().codigo)
            text += '|'
            actual = actual.getSiguiente()
        print(text)

    def imprimirMatriz(self):
        actual = self.cabecera
        while actual != None:
            actual.getPatron().imprimirCelda()
            actual = actual.getSiguiente()

    def imprimirLista(self):
        actual = self.cabecera
        while actual != None:
            actual.getPatron().imprimirCelda()
            actual = actual.getSiguiente()

    # GRAFICANDO CON GRAPHVIZ
    def graficaMatriz(self, nombre):
        dot = Graph(comment='pisosArtesanales')
        dot.attr(rankdir='LR')

        actual = self.cabecera
        Contador = 0
        while actual != None:
            auxiliar = actual.getPatron().cabecera
            Contador1 = 0
            while auxiliar != None:
                Contador += 1
                Contador1 += 1
                dot.node(str(Contador), str(auxiliar.getPatron().codigo))
                auxiliar = auxiliar.getSiguiente()
                if (Contador1 > 1):
                    dot.edge(str(Contador - 1), str(Contador))
                if Contador > (actual.getPatron().tamanio()):
                    a = Contador - (actual.getPatron().tamanio())
                    dot.edge(str(Contador), str(a), constraint='false')
            actual = actual.getSiguiente()
            dot.node('titulo', nombre + ' :', shape="plaintext", align="center")
        dot.render(nombre, format="pdf", view=True)

    def graficaPisos(self, p):
        actual = self.cabecera
        bus = 1
        while actual != None:
            if bus == p:
                actual.getPatron().celdas.graficaMatriz(actual.getPatron().nombre)
                input('Se generó la gráfica.\n')
                return
            bus += 1
            actual = actual.getSiguiente()
        input('\nElija una opcion correcta. Presione Enter para continuar.\n')

    def opcionImprimir(self, actual):
        actual = self.cabecera
        i = 1
        while actual != None:
            print(str(i)+'. '+actual.getPatron().codigo)
            i += 1
            actual = actual.getSiguiente()

    def Procesar(self, nombre0):
        actual = self.cabecera
        while actual != None:
            if (actual.getPatron()).nombre == nombre0:
                print('Se encontró el modelo del piso.')
                return 
            actual = actual.getSiguiente()
        return


    def buscarPiso(self, nombre0):
        actual = self.cabecera
        while actual != None:
            if (actual.getPatron()).nombre == nombre0:
                return actual.getPatron()
            actual = actual.getSiguiente()
        return None