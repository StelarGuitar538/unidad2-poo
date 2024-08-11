class Conexiones:
    __id: int
    __ip: str
    __nombreJuego: str
    __fecha: str
    __horaInicio: int
    __horaFin: int
    
    def __init__(self, id, ip, nombreJuego, fecha, horaInicio, horaFin):
        self.__id = id
        self.__ip = ip
        self.__nombreJuego = nombreJuego
        self.__fecha = fecha
        self.__horaInicio = horaInicio
        self.__horaFin = horaFin

    def getId(self):
        return self.__id

    def getIp(self):
        return self.__ip

    def getNombreJuego(self):
        return self.__nombreJuego

    def getFecha(self):
        return self.__fecha

    def getHoraInicio(self):
        return self.__horaInicio

    def getHoraFin(self):
        return self.__horaFin

    def __str__(self):
        return f"{self.__id};{self.__ip};{self.__nombreJuego};{self.__fecha};{self.__horaInicio};{self.__horaFin}"
    
    def __eq__(self, other):
        return (self.__id == other.getId() and
                self.__fecha == other.getFecha() and
                self.__horaInicio == other.getHoraInicio() and
                self.__ip != other.getIp())
        
    def __lt__(self, other):
        return (self.__id < other.getId() and
                self.__fecha < other.getFecha() and
                self.__horaInicio < other.getHoraInicio() and
                self.__ip < other.getIp())