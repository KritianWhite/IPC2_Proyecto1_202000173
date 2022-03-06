import os
import webbrowser
from matplotlib.pyplot import contour
from nodo import NodoDoble, nodoDoble_Patron

class listaPatron():
    def __init__(self):
        #-----Nodo Doble (listas)-----
        self.cabeza = NodoDoble()
        self.final = self.cabeza
        #-----Nodo Doble (patrones[celdas])-----
        #self.cabezaP = nodoDoble_Patron()
        #self.finalP = self.cabezaP


 #---------------ASIGNANDO NODO E INICIALIZANDO----------------
    def insertarPatron(self, nodoDobleNew):
        if self.cabeza.codigo is None:
            self.cabeza = nodoDobleNew
        elif self.cabeza.siguiente is None:
            self.cabeza.siguiente = nodoDobleNew
            nodoDobleNew.anterior = self.cabeza
            self.final = nodoDobleNew
        else: 
            self.final.siguiente = nodoDobleNew
            nodoDobleNew.anterior = self.cabeza
            self.final = nodoDobleNew

 #----------------RECORRIENDO LA LISTA-------------------------
    def recorriendoPatron(self):
        auxiliarNodo = self.cabeza
        cadena = ''
        while True:
            if auxiliarNodo.codigo is not None:
 #-----------GUARDANDO COORDENAS CODIGO Y PATRON-------------------------------------
                cadena += 'Código: ' + auxiliarNodo.codigo + 'Patron: ' + auxiliarNodo.patron
                if auxiliarNodo.siguiente is not None:
                    cadena += '\n'
                    auxiliarNodo = auxiliarNodo.siguiente
                else:
                    break
            else:
                break


 #class celdita()



class celdita:

    def __init__(self):
        #-----Nodo Doble (listas)-----
        #self.cabeza = NodoDoble()
        #self.final = self.cabeza
        #-----Nodo Doble (patrones[celdas])-----
        self.cabezaP = nodoDoble_Patron()
        self.finalP = self.cabezaP

 #================================================================================================================= usando nodoDoble_Patron()
    def insertarCelda(self, nodoDobleNewP):
        if self.cabezaP.CoordenadaXP is None:
            self.cabezaP = nodoDobleNewP
        elif self.cabezaP.siguienteP is None:
            self.cabezaP.siguienteP = nodoDobleNewP
            nodoDobleNewP.anteriorP = self.cabezaP
            self.finalP = nodoDobleNewP
        else: 
            self.finalP.siguienteP = nodoDobleNewP
            nodoDobleNewP.anteriorP = self.cabezaP
            self.finalP = nodoDobleNewP

 #----------------RECORRIENDO LA Patron-------------------------
    def recorriendoPatron(self):
        auxiliarNodoP = self.cabezaP
        cadenaP = ''
        while True:
            if auxiliarNodoP.CoordenadaXP is not None:
 #-----------GUARDANDO COORDENAS X Y Y, CODIGO, lETRA---------------
                cadenaP += 'Código: ' + str(auxiliarNodoP.codigoP) + 'Coordenada x: ' + str(auxiliarNodoP.CoordenadaXP) + 'Coordenada y: ' + str(auxiliarNodoP.CoordenadaYP) + 'Letra: ' + str(auxiliarNodoP.letraP)
                if not auxiliarNodoP.siguienteP != None:
                    cadenaP += '\n'
                    auxiliarNodop = auxiliarNodop.siguientep
                else:
                    break
            else:
                break

    def graficarMatriz(self):
        contador = 0
        contador1 = 0
        inicio = ""
        fin = ""
        auxiliar = self.cabezaP
        graph = "digraph G {\nrankdir = LR\n"

        while auxiliar is not None:
            if str(auxiliar.codigoP) == inicio:
                graph += "subgraph"
                graph += "{}".format(auxiliar.letraP)
                graph += "{\n"
                auxiliar = auxiliar.siguienteP
            contador1 += 1

            if auxiliar.letraP == "B" or auxiliar.letraP == "W":
                if auxiliar.letraP == "B":
                    color = "black"
                    color1 = "white"
                elif auxiliar.letraP == "W":
                    color = "white"
                    color1 = "black"
                graph += '{}[label = "{}", color = "black", fontcolor = "{}", fillcolor = "{}", style = "filled", shape = "box"];\n]'.format(contador1, contador1, color1, color )

                contador += 1
                auxiliar = auxiliar.siguienteP
            if  str(auxiliar.codigoP) == fin:
                graph += "}\n"
                auxiliar = auxiliar.siguienteP

        auxiliar = self.cabezaP
        contador2 = 1
        contador3 = 0
        while auxiliar is not None:
            if str(auxiliar.codigoP) == inicio:
                fil2 = int(auxiliar.CoordenadaXP)
                col2 = int(auxiliar.CoordenadaYP)
                auxiliar = auxiliar.siguienteP
            
            contador3 += 1
            if auxiliar.letraP == "B" or auxiliar.letraP =="W":
                for i in range(contador):
                    if (contador2 == 1 or contador2 == (contador2/2) + 1):
                        graph += "\nsubgraph cluster_" + str(0 if i == 0 else 1) + "{\nlabel=\"" + ("inicio" if i == 0 else "final") + "\"\nrankdir=TB\n"
                    if (contador2 == contador/2):
                        graph += "\n}"
                    if contador2%col2 == 0:
                        contador2 = contador2 + 1
                        continue
                    elif contador2 < contador:
                        graph += '{} -> {};\n'.format(contador2, contador2 + 1)
                        contador2 = contador2 + 1
                graph += "\n}"
                auxiliar = auxiliar.siguienteP
            if str(auxiliar.codigoP) == fin:
                auxiliar = auxiliar.siguienteP
        graph += "}"

 #-----------------------GUARDAR PINCELAZOS---------------------
        doctxt = "Grafica" + str(contador) + ".txt"
        with open(doctxt, 'w') as grafica:
            grafica.write(graph)
        pdf = "Grafica" + str(contador) + ".pdf"
        os.system("dot -Tpdf " + doctxt + " -o " + pdf)
        webbrowser.open(pdf)
