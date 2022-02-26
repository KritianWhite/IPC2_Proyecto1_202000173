from tkinter import Label
from tkinter.constants import ACTIVE, TRUE
from nodo import Nodo, nodo
from graphviz import Diagraph, Graph

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
                contador = contador + 1
                actual = actual.getSiguiente()
        return contador
    
    

