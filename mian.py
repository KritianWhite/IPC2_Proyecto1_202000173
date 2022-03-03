from tkinter import filedialog
import xml.etree.ElementTree as ET
from lista import lista
import ast

class Posicion(object):
    def __init__(self, x, y) -> None:
        self.R = x
        self.C = y
        self.anterior = None 
        self.siguiente = None
        

class Celda(Posicion):
    def __init__(self, x, y, costo) -> None:
        super().__init__(x, y)
        self.costo = costo

class Pisos(object):
    def __init__(self, nombre, filas, columnas, celdas, flipe, slide) -> None:
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas 
        self.celdas = celdas 
        self.flipe = flipe 
        self.slide = slide
        self.siguiente = None 

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


#-----------------MENU--------------------
global arrayMatriz
arrayMatriz = []

if __name__ == "__main__":
    opcion = ''
    pisos = lista()
    proceso = None

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
                input('\nLa extensión del archivo es incorrecta, presione enter para continuar.\n')
                continue

            documento = ET.parse(file)
            root = documento.getroot()
            #pisosLeidos = root.findall('piso')
            #print(documento)
            #print("hola")
            #---------LEENDO EL ARCHIVO--------------
            for pisos in root.iter("pisosArtesanales"):
                for piso in root.iter("piso"):
                
                    #print("hola1")
                    nombre = piso.attrib['nombre']
                    #print('Nombre: {}'.format(nombre))

                    for R,C,F,S, patrones in zip(piso.iter('R'), piso.iter('C'), piso.iter('F'), piso.iter('S'), piso.iter('patrones')):
                        #print('R: {} C: {} F: {} S: {}'.format(R.text, C.text, F.text, S.text))
                        for patron in patrones.iter('patron'):
                            #print('Codigo: {} Patron: {}'.format(patron.attrib['codigo'],patron.text))
                            patron = str(patron.text)
                            print(patron)

                            #MATRIZ
                            #for celdas in range(len(patron)):
                            for celdas in patron:
                                arrayMatriz.append(celdas)
                                print(arrayMatriz)
                                #auxiliarmatriz = patron[celdas]
                            #print(auxiliarmatriz)




                            
                            '''Celdas = lista()
                            for matrizFila in range(1, int(R.text)+1):
                                print('hola2')
                                nuevaFila = lista()
                                for matrizColumna in range (1, int(C.text)+1):
                                    for posicion in patrones:
                                        x1 = int(R.text)
                                        y1 = int(C.text)
                                        if x1 == matrizFila and y1 == matrizColumna:
                                            costo = int(posicion.text)
                                            nuevaCelda = Celda(x1,y1,costo)
                                            nuevaFila.Agregar(nuevaCelda)
                                Celdas.Agregar(nuevaFila)
                                   '''          
                '''
                print(nombre)
                #DIMENSIONES DEL AREA DE PISOS
                dimensionPisos = i.findall('piso')
                R = R
                print(R)
                #print(dimensionPisos)
                #R = i.findall('R')
                for j in i:
                    R = j.findall('R')
                    print(R)
                    C = j.findall('C')
                    print(C)
                    F = j.findall('F')
                    print(F)
                    S = j.findall('S')
                    print(S)
                
                #MATRIZ
                #patron = i.text
                #posiciones = i.findall('posicion')
                #celdas = lista()
                #for j in range(1, int(R+1)):
                #    newRow = lista()
                #    for k in range(1, int(C+1)):
                #        for pos in posiciones:
                #            lista(patron[j][k])
                #        print(lista())
                #        print('hola2')
                '''
        elif opcion == '2':
            print('\nVuelva pronton..!\n')
            break
        else: 
            input('\nElija una opcion válida. Presione enter para continuar.\n')