class Alquiler:
    __nombrePersonaAlquilada: str
    __idCanchaAlquilada: str
    __horaAlquilada: str
    __minutosAlquilada: str
    __minutosTotales: str
    
    def __init__(self, nombrePersonaAlquilada, idCanchaAlquilada, horaAlquilada, minutosAlquilada, minutosTotales):
        self.__nombrePersonaAlquilada = nombrePersonaAlquilada
        self.__idCanchaAlquilada = idCanchaAlquilada
        self.__horaAlquilada = horaAlquilada
        self.__minutosAlquilada = minutosAlquilada
        self.__minutosTotales = minutosTotales
        
    def getNombrePersonaAlquilada(self):
        return self.__nombrePersonaAlquilada
    
    def getIdCanchaAlquilada(self):
        return self.__idCanchaAlquilada
    
    def getHoraAlquilada(self):
        return self.__horaAlquilada
    
    def getMinutosAlquilada(self):
        return self.__minutosAlquilada
    
    def getMinutosTotales(self):
        return self.__minutosTotales
    
    def __str__(self):
        return f"{self.__nombrePersonaAlquilada} {self.__idCanchaAlquilada} {self.__horaAlquilada} {self.__minutosAlquilada} {self.__minutosTotales}"
    
    def __gt__ (self, other):
        return (self.__horaAlquilada, self.__minutosAlquilada) > (other.__horaAlquilada, other.__minutosAlquilada)
    