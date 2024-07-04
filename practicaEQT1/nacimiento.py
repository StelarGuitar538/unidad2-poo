class Nacimiento:
    __dniMama: str
    __tipoDeParto: str
    __fechaNacimiento: str
    __horaNacimiento: str
    __peso: str
    __alturaEnCm: int
    
    def __init__(self, dniMama, tipoDeParto, fechaNacimiento, horaNacimiento, peso, alturaEnCm):
        self.__dniMama = dniMama
        self.__tipoDeParto = tipoDeParto
        self.__fechaNacimiento = fechaNacimiento
        self.__horaNacimiento = horaNacimiento
        self.__peso = peso
        self.__alturaEnCm = alturaEnCm
        
    def getDNIMama(self):
        return self.__dniMama
    
    def getTipoDeParto(self):
        return self.__tipoDeParto
    
    def getFechaNacimiento(self):
        return self.__fechaNacimiento
    
    def getHoraNacimiento(self):
        return self.__horaNacimiento
    
    def getPeso(self):
        return self.__peso
    
    def getAlturaEnCm(self):
        return self.__alturaEnCm
    
    def __str__(self):
        return f"{self.__dniMama} {self.__tipoDeParto} {self.__fechaNacimiento} {self.__horaNacimiento} {self.__peso} {self.__alturaEnCm}"
    
    def __eq__(self, other):
        return (self.__dniMama, self.__fechaNacimiento) == (other.__dniMama, other.__fechaNacimiento)