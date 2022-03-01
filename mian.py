from tkinter import filedialog
import xml.etree.ElementTree as ET
from lista import lista


#class posicion(object):
#    def __init__(self, x, y):
#        self.x = x 
#        self.y = y

#class Celda(posicion):
#    def __init__(self, x, y, costo):
#        super().__init__(x, y)
#        self.costo = costo

class Pisos(object):
    def __init__(self, nombre, r, c, f, s, celdas):
        self.nombre = nombre
        self.row = r
        self.column = c
        self.flipe = f 
        self.slide = s
        self.celdas = celdas

class Patrones(Pisos):
    def __init__(self, nombre, r, c, f, s, codigo, costo, patron, x, y):
        super().__init__(nombre, r, c, f, s)
        self.patron = patron
        #self.codigo = codigo
        #self.costo = costo
        #self.x = x 
        #self.y = y 

#-----------------MENU--------------------
if __name__ == "__main__":
    opcion = ''
    pisos = lista()
    proceso = None

    while True:
        print('')
        print('1. Cargar Archivo.')
        print('2. Salir.')
        print('')

        opcion = input('Ingrese un número del menú')
        if opcion == '1':
            pisos = lista()
            proceso = None
            file = filedialog.askopenfilename()
            extension = file.split('.')

            if extension[len(extension)-1] != 'xml' and extension[len(extension)-1] != 'XML':
                input('\nArchivo con extensión incorrecta, presione enter para continuar.\n')
                continue

            documento = ET.parse(file)
            root = documento.getroot()
            pisosLeidos = root.findall('pisosArtesanales')

            #---------LEENDO EL ARCHIVO--------------
            for i in pisosLeidos:
                #NOMBRE
                nombre = i.attrib.get('nombre')
                #DIMENSIONES DEL AREA DE PISOS
                dimensionPisos = i.findall('piso')
                R = int((dimensionPisos[0].findall('R'))[0].text)
                C = int((dimensionPisos[0].findall('C'))[0].text)
                F = int(F.findall('F').text)
                S = int(S.findall('S').text)
                
                #MATRIZ
                patron = patron.findall('patron').text
                posiciones = i.findall('posicion')
                celdas = lista()
                for j in range(1, R+1):
                    newRow = lista()
                    for k in range(1, C+1):
                        for pos in posiciones:
                            lista(patron[j][k])

