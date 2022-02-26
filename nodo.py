class Nodo:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.siguiete = None

    def getDato(self):
        return self.dato

    def getSiguiente(self):
        return self.siguiete    

    def setDato(self, datoNuevo):
        self.dato = datoNuevo

    def setSiguiente(self, siguienteNew):
        self.siguiete = siguienteNew