from tkinter import filedialog
import xml.etree.ElementTree as ET

from nodo import nodoDoble_Patron, NodoDoble, nodoSimple
from ListaPisos import pisoss, listaSimple


# -----------------MENU--------------------

if __name__ == "__main__":
    opcion = ''

    while True:
        print(' ________________________________ ')
        print('|        MENU PRINCIPAL          |')
        print('|                                |')
        print('|   |> 1. Cargar Archivo.        |')
        print('|   |> 2. Salir.                 |')
        print('|                                |')
        print('|________________________________|')

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
                print(' ____________________________________________ ')
                print('|                SUB-MENU                    |')
                print('|                                            |')
                print('|    |> 1. Leer archivo y gráficar.          |')
                print('|    |> 2. Regresar al menú principal.       |')
                print('|____________________________________________|')

                opcion2 = input('\nIngrese un número del menú.\n')
                if opcion2 == '1':

                    # ---------LEENDO EL ARCHIVO--------------
                    for pisos in root.iter("pisosArtesanales"):
                        for piso in root.iter("piso"):
                            id = 0
                            nombre1 = piso.attrib['nombre']
                            #print('Nombre: {}'.format(nombre1))

                            for R, C, F, S, patrones in zip(piso.iter('R'), piso.iter('C'), piso.iter('F'), piso.iter('S'), piso.iter('patrones')):
                                Row = str(R.text)
                                Column = str(C.text)
                                Flipe = str(F.text)
                                Slide = str(S.text)
                                tmpPisos = pisoss(nombre1, Row, Column, Flipe, Slide)
                                listaPisos.insertarLP(tmpPisos)
                                #print('\nR: {} C: {} F: {} S: {}'.format(R, C, F, S))
                                #print('\nR: {} C: {} F: {} S: {}'.format(R.text, C.text, F.text, S.text))

                                for patron1 in patrones.iter('patron'):
                                    id += 1
                                    codigo1 = str(format(patron1.attrib['codigo']))
                                    #print('\nCodigo: '+codigo1)
                                    patron2 = str(patron1.text)
                                    #print('Patron: ' + patron2)
                                    #print('Codigo: {} Patron: {}'.format(patron.attrib['codigo'],patron.text)
                                    tmpPisos.celdas.insertarCelda(nodoDoble_Patron(-44, Row, Column, codigo1))
                                    contadorAux = 0
                                    for filat in range(int(Row)):
                                        for columnat in range(int(Column)):
                                            tmpNodo = nodoDoble_Patron(id, filat, columnat, patron2[contadorAux])
                                            tmpPisos.celdas.insertarCelda(tmpNodo)
                                            contadorAux += 1
                                    tmpPisos.celdas.insertarCelda(nodoDoble_Patron(-45,-45,-45, codigo1))
                                    tmpNodo2 = NodoDoble(codigo1, patron2)
                                    tmpPisos.patron.insertarPatron(tmpNodo2)
                                tmpPisos.celdas.recorriendoCelda()
                                #print('Termina el patron')
                                tmpPisos.patron.recorriendoPatron()
                                tmpPisos.celdas.graficarMatriz()
                            listaPisos.mostrar()
                
                elif opcion2 == '2':
                    break
                else:
                    input('\nIngrese un valor valido. Presione enter para continuar.\n')

        elif opcion == '2':
            print('\nVuelva pronton..!\n')
            break
        else:
            input('\nElija una opcion válida. Presione enter para continuar.\n')
