class Cliente:
    __nombre: str
    __apellido: str
    __dni: str
    __numeroTarjeta: int
    __saldoAnterior: int
    
    def __init__(self, nombre, apellido, dni, numeroTarjeta, saldoAnterior):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__numeroTarjeta = numeroTarjeta
        self.__saldoAnterior = saldoAnterior
        
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getDni(self):
        return self.__dni
    def getNumeroTarjeta(self):
        return self.__numeroTarjeta
    def getSaldoAnterior(self):
        return self.__saldoAnterior
    def setSaldo(self, saldo):
        self.__saldoAnterior = saldo
    
    def __str__(self):
        return f"{self.__nombre} {self.__apellido} {self.__dni} {self.__numeroTarjeta} {self.__saldoAnterior}"