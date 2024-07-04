from abc import ABC, abstractmethod
class Equipo:
    __marca: str
    __modelo: str
    __anoFabricaion: int
    __tipoCombustible: str
    __potencia: int
    __capacidadDeCarga: int
    __tarifaDiaria: float
    __diasAlquiler: int

    def __init__(self, marca, modelo, anoFabricaion, tipoCombustible, potencia, capacidadDeCarga, tarifaDiaria, diasAlquiler):
        self.__marca = marca
        self.__modelo = modelo
        self.__anoFabricaion = anoFabricaion
        self.__tipoCombustible = tipoCombustible
        self.__potencia = potencia
        self.__capacidadDeCarga = capacidadDeCarga
        self.__tarifaDiaria = tarifaDiaria
        self.__diasAlquiler = diasAlquiler

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getAnoFabricaion(self):
        return self.__anoFabricaion

    def getTipoCombustible(self):
        return self.__tipoCombustible

    def getPotencia(self):
        return self.__potencia

    def getCapacidadDeCarga(self):
        return self.__capacidadDeCarga

    def getTarifaDiaria(self):
        return self.__tarifaDiaria

    def getDiasAlquiler(self):
        return self.__diasAlquiler

    def __str__(self):
        return f"{self.__marca}, {self.__modelo}, {self.__anoFabricaion}, {self.__tipoCombustible}, {self.__potencia}, {self.__capacidadDeCarga}, {self.__tarifaDiaria}, {self.__diasAlquiler}"
    
    @abstractmethod
    def tarifaAlquiler(self):
        pass