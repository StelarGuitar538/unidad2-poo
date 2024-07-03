class Visualizacion:
    __idMiembro: int
    __idPeliculaQueVio: int
    __fecha: str
    __hora: str
    __minutos: int
    
    def __init__(self, idMiembro, idPeliculaQueVio, fecha, hora, minutos):
        self.__idMiembro = idMiembro
        self.__idPeliculaQueVio = idPeliculaQueVio
        self.__fecha = fecha
        self.__hora = hora
        self.__minutos = minutos
    
    def getIdMiembro(self):
        return self.__idMiembro
    
    def getIdPeliculaQueVio(self):
        return self.__idPeliculaQueVio
    
    def getFecha(self):
        return self.__fecha
    
    def getHora(self):
        return self.__hora
    
    def getMinutos(self):
        return self.__minutos
    
    def __str__(self):
        return f"{self.__idMiembro} {self.__idPeliculaQueVio} {self.__fecha} {self.__hora} {self.__minutos}"
    
    def __eq__(self, other):
        return (self.__idMiembro == other.__idMiembro and 
                self.__fecha == other.__fecha and 
                self.__hora == other.__hora)