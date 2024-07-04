from equipos import Equipo
class Maquinaria(Equipo):
    __tipoMaquinaria: str
    __peso: int
    
    def __init__(self, marca, modelo, anoFabricaion, tipoCombustible, potencia, capacidadDeCarga, tarifaDiaria, diasAlquiler, tipoMaquinaria, peso):
        super().__init__(marca, modelo, anoFabricaion, tipoCombustible, potencia, capacidadDeCarga, tarifaDiaria, diasAlquiler)
        self.__tipoMaquinaria = tipoMaquinaria
        self.__peso = peso

    def getTipoMaquinaria(self):
        return self.__tipoMaquinaria

    def getPeso(self):
        return self.__peso

    def __str__(self):
        return f"{self.getMarca()}, {self.getModelo()}, {self.getAnoFabricaion()}, {self.getTipoCombustible()}, {self.getPotencia()}, {self.getCapacidadDeCarga()}, {self.getTarifaDiaria()}, {self.getDiasAlquiler()}, {self.__tipoMaquinaria}, {self.__peso}"
    
    
    def tarifaAlquiler(self):
        if self.__peso <= 10:
            tarifa = self.getTarifaDiaria() * self.getDiasAlquiler()
        elif self.__peso > 10:
            tarifa = (self.getTarifaDiaria() * (self.getDiasAlquiler())) * 1.2
        return tarifa