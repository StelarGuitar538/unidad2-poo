class Cabana:
    __numero: int
    __cantidadHabitaciones: int
    __cantidadDeCamasGrandes: int
    __cantidadDeCamasPequenas: int
    __importePorDia: float
    
    def __init__(self, numero, cantidadHabitaciones, cantidadDeCamasGrandes, cantidadDeCamasPequenas, importePorDia):
        self.__numero = numero
        self.__cantidadHabitaciones = cantidadHabitaciones
        self.__cantidadDeCamasGrandes = cantidadDeCamasGrandes
        self.__cantidadDeCamasPequenas = cantidadDeCamasPequenas
        self.__importePorDia = importePorDia
        
    def getNumero(self):
        return self.__numero
    
    def getCantidadHabitaciones(self):
        return self.__cantidadHabitaciones
    
    def getCantidadDeCamasGrandes(self):
        return self.__cantidadDeCamasGrandes
    
    def getCantidadDeCamasPequenas(self):
        return self.__cantidadDeCamasPequenas
    
    def getImportePorDia(self):
        return self.__importePorDia
    
    def __str__(self):
        return f"{self.__numero} {self.__cantidadHabitaciones} {self.__cantidadDeCamasGrandes} {self.__cantidadDeCamasPequenas} {self.__importePorDia}"
    
    def __ge__(self, other):
        return (self.__cantidadDeCamasGrandes, self.__cantidadDeCamasPequenas, self.__importePorDia) > (other.__cantidadDeCamasGrandes, other.__cantidadDeCamasPequenas, other.__importePorDia)
    
    