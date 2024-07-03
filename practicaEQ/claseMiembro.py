class Miembro:
    __idMiembro: int
    __nya: str
    __mail: str
    
    def __init__(self, id, nya, mail):
        self.__idMiembro = id
        self.__nya = nya
        self.__mail = mail
    
    def getId(self):
        return self.__idMiembro
    
    def getNya(self):
        return self.__nya
    
    def getMail(self):
        return self.__mail
    
    def __str__(self):
        return f"{self.__idMiembro} {self.__nya} {self.__mail}"
    