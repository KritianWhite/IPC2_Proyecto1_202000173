class Nodo:
    def __init__(self, patron):
        self.patron = patron
        self.siguiete = None

    def getPatron(self):
        return self.patron

    def getSiguiente(self):
        return self.siguiete    

    def setPatron(self, patronNuevo):
        self.patron = patronNuevo

    def setSiguiente(self, siguienteNew):
        self.siguiete = siguienteNew