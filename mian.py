from tkinter import filedialog
import xml.etree.ElementTree as ET
from lista import lista


class posicion(object):
    def __init__(self, x, y):
        self.x = x 
        self.y = y

class celdita(posicion):
    def __init__(self, x, y, costo):
        super().__init__(x, y)
        self.costo = costo

class Pisos(object):
    def __init__(self, nombre, r, c, f, s):
        self.nombre = nombre
        self.row = r
        self.colum = c
        self.flipe = f 
        self.slide = s

class Patrones(Pisos):
    def __init__(self, nombre, r, c, f, s, codigo):
        super().__init__(nombre, r, c, f, s)
        self.codigo = codigo

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
                input('\nArchivo con extensión incorrecta, presione enter para continaur.')
                continue

            documento = ET.parse(file)
            root = documento.getroot()
            pisosLeidos = root.findall('pisosArtesanales')

            #---------LEENDO EL ARCHIVO--------------
            for i in pisosLeidos:
                #NOMBRE
                nombre = i.attrib.get('nombre')
                #FILAS
                r = i.attrib.get('R')
                #COLUMNA
                c = i.attrib.get('C')
                #FLIPE = VOLTEAR
                f = i.attrib.get('F')
                #SLIDE = CORRER/INTERCAMBIAR
                s = i.attrib.get('S')
                #PATRONES
                patrones = i.attrib.get('patrones')
                #CODIGO
                codigo = i.attrib.get('codigo')




