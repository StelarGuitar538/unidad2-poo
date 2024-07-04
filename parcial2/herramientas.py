from equipos import Equipo
class Herramientas(Equipo):
    __tipoHerramientas: str
    
    def __init__(self, marca, modelo, anoFabricaion, tipoCombustible, potencia, capacidadDeCarga, tarifaDiaria, diasAlquiler, tipoHerramientas):
        super().__init__(marca, modelo, anoFabricaion, tipoCombustible, potencia, capacidadDeCarga, tarifaDiaria, diasAlquiler)
        self.__tipoHerramientas = tipoHerramientas

    def getTipoHerramientas(self):
        return self.__tipoHerramientas

    def __str__(self):
        return f"{self.getMarca()}, {self.getModelo()}, {self.getAnoFabricaion()}, {self.getTipoCombustible()}, {self.getPotencia()}, {self.getCapacidadDeCarga()}, {self.getTarifaDiaria()}, {self.getDiasAlquiler()}, {self.__tipoHerramientas}"
    
    def tarifaAlquiler(self):
        if self.__tipoHerramientas == "bateria":
            tarifa = (self.getTarifaDiaria() * self.getDiasAlquiler()) * 1.1
        elif self.__tipoHerramientas == "cable":
            tarifa = (self.getTarifaDiaria() * self.getDiasAlquiler())
        return tarifa