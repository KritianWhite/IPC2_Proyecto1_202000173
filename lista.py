from tkinter import Label
from tkinter.constants import ACTIVE, TRUE
from nodo import Nodo
from graphviz import Digraph, Graph

class lista:
    def __init__(self) -> None:
        self.cabecera = None

    def Colocar(self, articulo):
        temp = Nodo(articulo)
        temp.setSiguiente(self.cabecera)
        self.cabecera = temp
    
    def Agregar(self, articulo):
        if not self.cabecera:
            self.cabecera = Nodo(articulo)
            return
        correrPiso = self.cabecera
        while correrPiso.siguiete:
            correrPiso = correrPiso.siguiete
        correrPiso.siguiete = Nodo(articulo)

    def tamanio(self):
        actual = self.cabecera
        contador = 0
        if actual != None:
            while actual !=None:
                contador += 1
                actual = actual.getSiguiente()
        return contador
    

    
    def remover(self, articulo):
        actual = self.cabecera
        antes = None
        localizado = False
        while not localizado:
            if actual.getPatron() == articulo:
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
            text += str(actual.getPatron())
            text += '|'
            actual = actual.getSiguiente()
        print(text)

    def imprimirLista(self):
        actual = self.cabecera
        while actual != None:
            actual.getPatron().imprimirCelda()
            actual = actual.getSiguiente()

    def imprimirLista(self):
        actual = self.cabecera
        while actual != None:
            print(actual.getPatron())
            actual = actual.getSiguiente()

    #def graficarMatriz(self, nombre):


    

