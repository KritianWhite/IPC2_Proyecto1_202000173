from tkinter import filedialog
import xml.etree.ElementTree as ET
from lista import lista


class Posicion(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.anterior = None
        self.siguiente = None

# PATRON
class Celda(Posicion):
    def __init__(self, x, y, codigo):
        super().__init__(x, y)
        self.codigo = codigo


class Pisos(object):
    def __init__(self, nombre, filas, columnas, flipe, slide, codigo):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.celdas = celdas
        self.flipe = flipe
        self.slide = slide
        self.codigo = codigo
        #self.matrizA = lista()

'''
class Pisos(object):
    def __init__(self, nombre = None, r = None, c = None, f = None, s = None):
        self.nombre = nombre
        self.row = r
        self.column = c
        self.flipeCost = f 
        self.slidecost = s
        self.listapatrones = lista()
        self.siguiente = None 
        self.anterior = None

class Patrones(Pisos):
    def __init__(self, nombre=None, r=None, c=None, f=None, s=None, codigo = None, costo = None):
        super().__init__(nombre, r, c, f, s)
        self.codigo = codigo
        self.costo = costo 

class Patron(Patrones):
    def __init__(self, nombre=None, r=None, c=None, f=None, s=None, codigo=None, costo=None, patrones = None):
        super().__init__(nombre, r, c, f, s, codigo, costo)
        self.patrones = patrones
        self.siguiente = None
'''

##############

'''
class Posicion(Pisos):
    def __init__(self, nombre, r, c, f, s):
        super().__init__(nombre, r, c, f, s)
    

    #def __init__(self, R, C):
    #    self.R = R 
    #    self.C = C 

class Celda(Posicion):
    def __init__(self, R, C, Costo):
        super().__init__(R, C)
        self.Costo = Costo

class Patron(Pisos):
    def __init__(self, nombre, r, c, f, s, codigo, cadena):
        super().__init__(nombre, r, c, f, s)
        self.codigo = codigo 
        self.cadena = cadena 

class listaPatrones():
    def __init__(self) -> None:
        pass

class Matriz():
    def __init__(self) -> None:
        pass

#class Patrones(Pisos):
#    def __init__(self, nombre, r, c, f, s, codigo, costo, patron, x, y):
#        super().__init__(nombre, r, c, f, s)
#       self.patron = patron
#       self.codigo = codigo
        #self.costo = costo
        #self.x = x 
        #self.y = y 
'''


# -----------------MENU--------------------
global arrayMatriz
arrayMatriz = []

if __name__ == "__main__":
    opcion = ''
    #pisos = lista()
    #proceso = None

    while True:
        print('')
        print('1. Cargar Archivo.')
        print('2. Salir.')
        print('')

        opcion = input('\nIngrese un número del menú:\n')
        if opcion == '1':
            pisos = lista()
            proceso = None
            file = filedialog.askopenfilename()
            extension = file.split('.')

            if extension[len(extension)-1] != 'xml' and extension[len(extension)-1] != 'XML':
                input(
                    '\nLa extensión del archivo es incorrecta, presione enter para continuar.\n')
                continue

            documento = ET.parse(file)
            root = documento.getroot()
            print('\nEl archivo se cargó correctamente.\n')

            pisosList = lista()
            pisosList2 = lista()
            Procesop = None
            while True:

                print('')
                print('1. Mostrar gráficamente el patron')
                print('2. Seleccionar nuevo código de patron.')
                print('3. Regresar al menú principal.')
                print('')

                opcion2 = input('\nIngrese un número del menú.\n')
                if opcion2 == '1':

                    #pisosLeidos = root.findall('piso')
                    # print(documento)
                    # print("hola")
                    # ---------LEENDO EL ARCHIVO--------------
                    for pisos in root.iter("pisosArtesanales"):
                        for piso in root.iter("piso"):

                            # print("hola1")
                            nombrex = piso.attrib['nombre']
                            #print('Nombre: {}'.format(nombre))

                            for R, C, F, S, patrones in zip(piso.iter('R'), piso.iter('C'), piso.iter('F'), piso.iter('S'), piso.iter('patrones')):
                                R = str(R.text)
                                R1 = int(R)
                                C = str(C.text)
                                C1 = int(C)  
                                F = str(F.text)
                                F1 = int(F)
                                S = str(S.text)
                                S1 = int(S)
                                #print('R: {} C: {} F: {} S: {}'.format(R.text, C.text, F.text, S.text))
                                for patron in patrones.iter('patron'):
                                    #print('Codigo: {} Patron: {}'.format(patron.attrib['codigo'],patron.text))
                                    codigox = format(patron.attrib['codigo'])
                                    codigox = str(codigox)
                                    patron = str(patron.text)
                                    listax = [celdas1 for celdas1 in patron]
                                    matrizx = []
                                    for o in range(0, len(listax), C1):
                                        matrizx = listax[o:o+C1]
                                    #print(matrizx)


                                    #celdas.Agregar(listax)
                                    
                                    # POSICION INICIAL
                                    x = 0
                                    y = 0
                                    posicionInicial = Posicion(x,y)
                                    # POSICION FINAL
                                    x2 = R1
                                    y2 = C1 
                                    posicionFinal = Posicion(x2, y2)
                                    
                                    # ARMANDO MATRIZ
                                    celdas = lista()
                                    for fil in range(1, R1+1):
                                        nuevaFila = lista()
                                        for col in range(1, C1+1):
                                            for array in matrizx:
                                                coorX = R1
                                                coorY = C1
                                                if coorX == fil and coorY == col:
                                                    gastoF = F1
                                                    gastoS = S1
                                                    nuevaCelda = Celda(coorX, coorY, codigox)
                                                    #print('\nCoorX: ' + str(nuevaCelda.x) + '\nCoorY: ' + str(nuevaCelda.y) + '\nCodigo: ' + nuevaCelda.codigo)
                                                    nuevaFila.Agregar(nuevaCelda)
                                                    break
                                        celdas.Agregar(nuevaFila)

                                    #celdas.imprimirMatriz()
                                    #print(nuevaFila.Agregar(nuevaCelda))
                                    #celdas.graficaMatriz(nombrex)
                                    #print(nuevaFila)


                            #nuevoPiso = Pisos(nombre, R, C, celdas, F, S)
                            nuevoPiso = Pisos(nombrex,R,C,F,S,codigox)
                            print('\nNombre: ' + nuevoPiso.nombre + '\nFila: ' + str(nuevoPiso.filas) + '\nColumna: ' + str(nuevoPiso.columnas) + '\nFlipe: ' + str(nuevoPiso.flipe) + '\nSlide: ' + str(nuevoPiso.slide) + '\nCodigo: ' + nuevoPiso.codigo)
                            pisosList.Agregar(nuevoPiso)
                            pisosList2.Agregar(nuevaCelda)

                    # OPCION PARA PODER GRAFICAR LOS NODOS HACIENDO REFERENCIA A LOS METODOS DE LA CLASS lista()
                    if pisosList2.tamanio() == 0:
                        input('\nNo se encontraron pisos. Presione Enter para continuar.\n')
                    else: 
                        print('\nElija el Piso que quiere gráficar.')
                        pisosList2.opcionImprimir(codigox)
                        opcion3 = input()
                    
                        if opcion3.isdigit():
                            opcion3 = int(opcion3)
                            pisosList2.graficaPisos(opcion3)
                        else:
                            input('Elija una opcion del menu.')

                
                elif opcion2 == '2':
                    '''
                    if pisosList.tamanio() == 0:
                        input('\nCargue un archivo con pisos. Presione Enter para continuar.\n')
                    else:
                        pisosList.opcionImprimir()
                        opcion4 = input()
                        if opcion4.isdigit():
                            pisosList.graficaPisos((opcion4))
                        else:               
                            input('\nElija un numero del menú. Presione Enter para continuar.\n')
                    '''
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
