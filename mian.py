from tkinter import filedialog
import xml.etree.ElementTree as ET

from nodo import nodoDoble_Patron, NodoDoble, nodoSimple
from ListaPisos import pisoss, listaSimple

''''
class Posicion(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.anterior = None
        self.siguiente = None

# PATRON
class Celda(Posicion):
    def __init__(self, x, y, cadena):
        super().__init__(x, y)
        self.cadena = cadena
        #self.cadena = lista()


class Pisos():
    def __init__(self, nombre, filas, columnas, flipe, slide):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.flipe = flipe
        self.slide = slide
'''


# -----------------MENU--------------------

if __name__ == "__main__":
    opcion = ''

    while True:
        print('')
        print('1. Cargar Archivo.')
        print('2. Salir.')
        print('')

        opcion = input('\nIngrese un número del menú:\n')
        if opcion == '1':
            file = filedialog.askopenfilename()
            extension = file.split('.')

            if extension[len(extension)-1] != 'xml' and extension[len(extension)-1] != 'XML':
                input(
                    '\nLa extensión del archivo es incorrecta, presione enter para continuar.\n')
                continue

            documento = ET.parse(file)
            root = documento.getroot()
            print('\nEl archivo se cargó correctamente.\n')

            listaPisos = listaSimple()
            #pisosList = lista()
            while True:

                print('')
                print('1. Leer archivo y gráficar.')
                print('3. Regresar al menú principal.')
                print('')

                opcion2 = input('\nIngrese un número del menú.\n')
                if opcion2 == '1':

                    # ---------LEENDO EL ARCHIVO--------------
                    for pisos in root.iter("pisosArtesanales"):
                        for piso in root.iter("piso"):
                            codigoP = 0
                            nombre1 = piso.attrib['nombre']
                            #print('Nombre: {}'.format(nombre1))

                            for R, C, F, S, patrones in zip(piso.iter('R'), piso.iter('C'), piso.iter('F'), piso.iter('S'), piso.iter('patrones')):
                                R = str(R.text)
                                C = str(C.text)
                                F = str(F.text)
                                S = str(S.text)
                                tmpPisos = pisoss(nombre1, R, C, F, S)
                                listaPisos.insertarLP(tmpPisos)
                                #print('\nR: {} C: {} F: {} S: {}'.format(R, C, F, S))
                                #print('\nR: {} C: {} F: {} S: {}'.format(R.text, C.text, F.text, S.text))

                                for patron1 in patrones.iter('patron'):
                                    codigoP += 1
                                    codigo1 = str(format(patron1.attrib['codigo']))
                                    print('\nCodigo: '+codigo1)
                                    patron2 = str(patron1.text)
                                    print('Patron: ' + patron2)
                                    #print('Codigo: {} Patron: {}'.format(patron.attrib['codigo'],patron.text)
                                    tmpPisos.celdas.insertarCelda(nodoDoble_Patron(-44, R, C, codigo1))
                                    contadorAux = 0
                                    for fila in range(int(R)):
                                        for columna in range(int(C)):
                                            tmpNodo = nodoDoble_Patron(codigoP, fila, columna, patron2)
                                            tmpPisos.celdas.insertarCelda(tmpNodo)
                                            contadorAux = contadorAux + 1
                                    tmpPisos.celdas.insertarCelda(nodoDoble_Patron(-45,-45,-45, codigo1))
                                    tmpNodo2 = NodoDoble(codigo1, patron2)
                                    tmpPisos.patron.insertarPatron(tmpNodo2)
                                tmpPisos.celdas.recorriendoPatron()
                                print('Termina el patron')
                                tmpPisos.patron.recorriendoPatron()
                                tmpPisos.celdas.graficarMatriz()
                            listaPisos.mostrar()
                                            

                    #----------------------------------------------------------------------------------------------#
                    # OPCION PARA PODER GRAFICAR LOS NODOS HACIENDO REFERENCIA A LOS METODOS DE LA CLASS lista()
                    '''
                    if pisosList.tamanio() == 0:
                        input('\nNo se encontraron pisos. Presione Enter para continuar.\n')
                    else: 
                        print('\nElija el Piso que quiere gráficar.')
                        pisosList.opcionImprimir(nombrex)
                        opcion3 = input()
                    
                        if opcion3.isdigit():
                            opcion3 = int(opcion3)
                            pisosList.graficaPisos(opcion3)
                        else:
                            input('Elija una opcion del menu.')
                    '''
                elif opcion2 == '2':
                    print('Hola 3')
                    continue
                    
                elif opcion2 == '3':
                    break
                else:
                    input('\nIngrese un valor valido. Presione enter para continuar.\n')

        elif opcion == '2':
            print('\nVuelva pronton..!\n')
            break
        else:
            input('\nElija una opcion válida. Presione enter para continuar.\n')
