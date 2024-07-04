class Mama:
    __dni: str
    __edad: int
    __nya: str
    
    def __init__(self, dni, edad, nya):
        self.__dni = dni
        self.__edad = edad
        self.__nya = nya
        
    def getDNI(self):
        return self.__dni
    
    def getEdad(self):
        return self.__edad
    
    def getNya(self):
        return self.__nya
    
    def __str__(self):
        return f"{self.__dni} {self.__edad} {self.__nya}"