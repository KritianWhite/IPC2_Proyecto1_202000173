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
    def recorriendoCelda(self):
        auxiliarNodoP = self.cabezaP
        cadenaP = ''
        while True:
            if auxiliarNodoP.CoordenadaXP is not None:
 #-----------GUARDANDO COORDENAS X Y Y, CODIGO, lETRA---------------
                cadenaP += "Código: " + str(auxiliarNodoP.id) + "Coordenada x: " + str(auxiliarNodoP.CoordenadaXP) + "Coordenada y: " + str(auxiliarNodoP.CoordenadaYP) + "Letra: " + auxiliarNodoP.letraP
                if not auxiliarNodoP.siguienteP != None:
                    cadenaP += "\n"
                    auxiliarNodop = auxiliarNodop.siguientep
                else:
                    break
            else:
                break

    def graficarMatriz(self):
        contador = 0
        contador1 = 0
        inicio = "-44"
        fin = "-45"
        auxiliarR = self.cabezaP
        graph = "digraph G {\nrankdir = LR\n"

        while auxiliarR is not None:
            if str(auxiliarR.id) == inicio:
                graph += "subgraph "
                graph += "{}".format(auxiliarR.letraP)
                graph += "{ \n"
                nombreAux = auxiliarR.letraP
                filaAux = int(auxiliarR.CoordenadaXP)
                ColumnaAux = int(auxiliarR.CoordenadaYP)

                auxiliarR = auxiliarR.siguienteP
            contador1 += 1
            if auxiliarR.letraP == "B" or auxiliarR.letraP == "W":
                if auxiliarR.letraP == "B":
                    color = "black"
                    color1 = "black"
                elif auxiliarR.letraP == "W":
                    color = "white"
                    color1 = "white"

                graph += '{}[label="{}", color = "black", fontcolor="{}", fillcolor="{}", style="filled", shape="box"];\n'.format(contador1, contador1, color, color1 )

                contador += 1
                #graph += '{}<-{};\n'.format(auxiliarR.letraP, auxiliarR.siguienteP)
                auxiliarR = auxiliarR.siguienteP
            if  str(auxiliarR.id) == fin:
                graph += "}\n"
                auxiliarR = auxiliarR.siguienteP

        auxiliarR = self.cabezaP
        contador2 = 1
        contador3 = 0
        while auxiliarR is not None:
            if str(auxiliarR.id) == inicio:
                fil2 = int(auxiliarR.CoordenadaXP)
                col2 = int(auxiliarR.CoordenadaYP)
                auxiliarR = auxiliarR.siguienteP
            
            contador3 += 1
            if auxiliarR.letraP == "B" or auxiliarR.letraP =="W":
                for q in range(contador):
                    if (contador2 ==  1 or contador2 == (contador/2) + 1):
                        graph += "\nsubgraph cluster_" + str(0 if q==0 else 1) + "{\nlabel=\"" + ("Patron inicial" if q==0 else "Patron final") + "\"\nrankdir=TB\n"
                    if (contador2 == contador/2):
                        graph += "\n}"
                    if contador2%col2 == 0:
                        contador2 += 1
                        continue
                    elif contador2 < (contador):
                        graph += '{}->{}[style="invis"];\n'.format(contador2, contador2 + 1)
                        contador2 += 1
                graph += "\n}"
                auxiliarR = auxiliarR.siguienteP
            if str(auxiliarR.id) == fin:
                auxiliarR = auxiliarR.siguienteP
        graph += "}"

 #-----------------------GUARDAR PINCELAZOS---------------------
        doctxt = "Grafica" + str(contador) + ".txt"
        with open(doctxt, 'w') as grafica:
            grafica.write(graph)
        pdf = "Grafica" + str(contador) + ".pdf"
        os.system("dot -Tpdf " + doctxt + " -o " + pdf)
        webbrowser.open(pdf)
        print("Se generó la gráfica correctamente.")
