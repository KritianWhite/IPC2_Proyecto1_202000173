class NodoDoble:
    def __init__(self, codigo = None, patron = None):
        self.codigo = codigo
        self.patron = patron
        self.anterior = None
        self.siguiente = None

class nodoDoble_Patron:
    def __init__(self, id = None, CoordenadaXP = None, CoordenadaYP = None, letraP = None):
        self.id = id
        self.CoordenadaXP = CoordenadaXP
        self.CoordenadaYP = CoordenadaYP
        self.letraP = letraP
        self.siguienteP = None
        self.anteriorP = None

class nodoSimple:
    def __init__(self, pisos = None):
        self.pisos = pisos 
        self.siguiente = None

