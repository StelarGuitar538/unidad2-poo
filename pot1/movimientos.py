class Movimiento:
    __numeroTarjeta: int
    __fecha: str
    __descripcion: str
    __tipoDeMovimiento: str
    __importe: int
    
    def __init__(self, numeroTarjeta, fecha, descripcion, tipoDeMovimiento, importe):
        self.__numeroTarjeta = numeroTarjeta
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tipoDeMovimiento = tipoDeMovimiento
        self.__importe = importe
        
    def getNumeroTarjeta(self):
        return self.__numeroTarjeta
    def getFecha(self):
        return self.__fecha
    def getDescripcion(self):
        return self.__descripcion
    def getTipoDeMovimiento(self):
        return self.__tipoDeMovimiento
    def getImporte(self):
        return self.__importe
    def __str__(self):
        return f"{self.__numeroTarjeta} {self.__fecha} {self.__descripcion} {self.__tipoDeMovimiento} {self.__importe}"
    
    def __lt__(self, other):
        return self.__numeroTarjeta < other.__numeroTarjeta