class Reserva:
    __numeroReserva: int
    __cliente: str
    __numeroCabana: int
    __fechaInicio: str
    __cantidadHuespedes: int
    __cantidadDias: int
    __sena: float
    
    def __init__(self, numeroReserva, cliente, numeroCabana, fechaInicio, cantidadHuespedes, cantidadDias, sena):
        self.__numeroReserva = numeroReserva
        self.__cliente = cliente
        self.__numeroCabana = numeroCabana
        self.__fechaInicio = fechaInicio
        self.__cantidadHuespedes = cantidadHuespedes
        self.__cantidadDias = cantidadDias
        self.__sena = sena
        
    def getNumeroReserva(self):
        return self.__numeroReserva
    
    def getCliente(self):
        return self.__cliente
    
    def getNumeroCabana(self):
        return self.__numeroCabana
    
    def getFechaInicio(self):
        return self.__fechaInicio
    
    def getCantidadHuespedes(self):
        return self.__cantidadHuespedes
    
    def getCantidadDias(self):
        return self.__cantidadDias
    
    def getSena(self):
        return self.__sena
    
    def __str__(self):
        return f"{self.__numeroReserva} {self.__cliente} {self.__numeroCabana} {self.__fechaInicio} {self.__cantidadHuespedes} {self.__cantidadDias} {self.__sena}"