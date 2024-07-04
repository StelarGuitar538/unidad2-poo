class Cancha:
    __id: str
    __tipoPiso: str
    __importePorHora: float
    
    def __init__(self, id, tipoPiso, importePorHora):
        self.__id = id
        self.__tipoPiso = tipoPiso
        self.__importePorHora = importePorHora
        
    def getId(self):
        return self.__id
    
    def getTipoPiso(self):
        return self.__tipoPiso
    
    def getImportePorHora(self):
        return self.__importePorHora
    
    def __str__(self):
        return f"{self.__id} {self.__tipoPiso} {self.__importePorHora}"
    
    