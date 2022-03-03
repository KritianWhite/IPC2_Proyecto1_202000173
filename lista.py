import webbrowser
import os
from tkinter import Label
from tkinter.constants import ACTIVE, TRUE
from turtle import shape
from nodo import Nodo
from graphviz import Digraph, Graph

class lista:
    '''
    def __init__(self) -> None:
        self.cabecera = None

    def Insertar(self, x):
        nuevoNodo = Nodo(x)
        if self.cabecera == None:
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
    
    def Colocar(self, x):
        temp = Nodo(x)
        temp.setSiguiente(self.cabecera)
        self.cabecera = temp
    
    def Agregar(self, x):
        if not self.cabecera:
            self.cabecera = Nodo(x)
            return
        correrPiso = self.cabecera
        while correrPiso.siguiete:
            correrPiso = correrPiso.siguiete
        correrPiso.siguiete = Nodo(x)
    
    def tamanio(self):
        actual = self.cabecera
        contador = 0
        if actual != None:
            while actual !=None:
                contador += 1
                actual = actual.getSiguiente()
        return contador
    

    
    def remover(self, x):
        actual = self.cabecera
        antes = None
        localizado = False
        while not localizado:
            if actual.getPatron() == x:
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
            text += str(actual.getPatron().costo)
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

    def graficaMatriz(self, nombre):
        dot = Graph(comment='Pisos')
        dot.attr(rankdir='LR')
        actual = self.cabecera
        Contador = 0
        while actual != 0:
            auxiliar = actual.getPatron().cabecera
            Contador1 = 0
            while auxiliar != None:
                Contador += 1
                Contador1 += 1
                dot.node(str(Contador), str(auxiliar.getPatron().costo))
                auxiliar = auxiliar.getSiguiente()
                if Contador1 > 1:
                    dot.edge(str(Contador - 1), str(Contador))
                if Contador > (actual.getPatron().tamanio()):
                    a = Contador - (actual.getPatron().tamanio())
                    dot.edge(str(Contador), str(a), constraint = 'false')
            actual = actual.getSiguiente()
            dot.node('titulo', nombre+ ':', shape='plaintext', align='center')
        dot.render(nombre, format='pdf', view=True)

def graficaPisos(self, p):
    actual = self.cabecera
    cel = 1
    while actual != None:
        if cel == p:
            actual.getPaton().celdas.graficaMatriz(actual.getPatron().nombre)
            input('Se generó la gráfica.\n')
            return
        cel += 1
        actual = actual.getSiguiente()
    input('Ocurrio un error. \n')



    

