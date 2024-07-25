class Gamer:
    __idJugador = int
    __dni = str
    __nombre = str
    __apellido = str
    __alias = str
    __plan = str
    __importeBasico = float
    __tiempoLimite = int
    
    
    def __init__(self, idJugador, dni, nombre, apellido, alias, plan, importeBasico, tiempoLimite):
        self.__idJugador = idJugador
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__alias = alias
        self.__plan = plan
        self.__importeBasico = importeBasico
        self.__tiempoLimite = tiempoLimite

    def getIdJugador(self):
        return self.__idJugador

    def getDni(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getAlias(self):
        return self.__alias

    def getPlan(self):
        return self.__plan    
    
    def getImporteBasico(self):
        return self.__importeBasico

    def getTiempoLimite(self):
        return self.__tiempoLimite
    
    def __str__(self):
        return f"{self.__idJugador} - {self.__dni} - {self.__nombre} - {self.__apellido} - {self.__alias} - {self.__plan} - {self.__importeBasico} - {self.__tiempoLimite}"