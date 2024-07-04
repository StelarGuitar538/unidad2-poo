from equipos import Equipo

class Nodo:
    __equipo: Equipo
    __sig: object
    
    def __init__(self, equipo):
        self.__equipo = equipo
        self.__sig = None
        
    def getEquipo(self):
        return self.__equipo

    def setSig(self, sig):
        self.__sig = sig

    def getSig(self):
        return self.__sig