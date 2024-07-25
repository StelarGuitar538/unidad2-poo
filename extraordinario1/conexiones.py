class Conexion:
    __idJugador = int
    __direccionIp = str
    __nombreDelJuego = str
    __fecha = str
    __horaDeInicio = str
    __horaDeFin = str
    
    def __init__(self, idJugador, direccionIp, nombreDelJuego, fecha, horaDeInicio, horaDeFin):
        self.__idJugador = idJugador
        self.__direccionIp = direccionIp
        self.__nombreDelJuego = nombreDelJuego
        self.__fecha = fecha
        self.__horaDeInicio = horaDeInicio
        self.__horaDeFin = horaDeFin

    def getIdJugador(self):
        return self.__idJugador

    def getDireccionIp(self):
        return self.__direccionIp

    def getNombreDelJuego(self):
        return self.__nombreDelJuego

    def getFecha(self):
        return self.__fecha

    def getHoraDeInicio(self):
        return self.__horaDeInicio

    def getHoraDeFin(self):
        return self.__horaDeFin
    
    def __str__(self):
        return f"{self.__idJugador} - {self.__direccionIp} - {self.__nombreDelJuego} - {self.__fecha} - {self.__horaDeInicio} - {self.__horaDeFin}"
    
    def __eq__(self, other):
        return (self.__idJugador == other.getIdJugador() and
                self.__fecha == other.getFecha() and 
                self.__horaDeInicio  == other.getHoraDeInicio() and
                self.__direccionIp != other.getDireccionIp())
    
    def __lt__(self, other):
        return (self.__idJugador < other.getIdJugador() and
                self.__fecha < other.getFecha() and 
                self.__horaDeInicio < other.getHoraDeInicio() and
                self.__direccionIp < other.getDireccionIp())