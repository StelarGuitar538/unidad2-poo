class Conexion:
    __idJugador = int
    __direccionIp = str
    __nombreJuego = str
    __fechaJuego = str
    __horaInicio = int
    __horaFin = int

    
    def __init__(self, idJugador, direccionIp, nombreJuego, fechaJuego, horaInicio, horaFin):
        self.__idJugador = idJugador
        self.__direccionIp = direccionIp
        self.__nombreJuego = nombreJuego
        self.__fechaJuego = fechaJuego
        self.__horaInicio = horaInicio
        self.__horaFin = horaFin

    def getIdJugador(self):
        return self.__idJugador
    
    def getDireccionIp(self):
        return self.__direccionIp
    
    def getNombreJuego(self):
        return self.__nombreJuego
    
    def getFechaJuego(self):
        return self.__fechaJuego
    
    def getHoraInicio(self):
        return self.__horaInicio
    
    def getHoraFin(self):
        return self.__horaFin
    
    def __str__(self):
        return f"{self.__idJugador};{self.__direccionIp};{self.__nombreJuego};{self.__fechaJuego};{self.__horaInicio};{self.__horaFin}"
    
    def __eq__(self, other):
        return (self.__idJugador == other.getIdJugador() and
                self.__fechaJuego == other.getFechaJuego() and 
                self.__horaInicio  == other.getHoraInicio() and
                self.__direccionIp != other.getDireccionIp())
        
    
    def __lt__(self, other):
        return (self.__idJugador < other.getIdJugador() and
                self.__fechaJuego < other.getFechaJuego() and 
                self.__horaInicio < other.getHoraInicio() and
                self.__direccionIp < other.getDireccionIp())
