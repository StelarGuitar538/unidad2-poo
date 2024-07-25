from conexiones import Conexion
import csv
import numpy as np

class GestorConexiones:
    __arregloConexiones = np.ndarray
    __cantidad = 0
    __dimension = 0
    __incremento = 1
    
    def __init__(self):
        self.__arregloConexiones = np.empty([0], dtype=Conexion)
        
    def agregar(self, conexion):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__arregloConexiones.resize(self.__dimension)
        self.__arregloConexiones[self.__cantidad] = conexion
        self.__cantidad += 1
        
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/u2 poo/extraordinario1/archivoscsv/conexiones.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            c = Conexion(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
            self.agregar(c)
        archivo.close()
        
    def mostrar(self):
        for c in self.__arregloConexiones:
            print(c)

    def inciso1(self, dni, gg):
        th = 0
        pos = gg.buscarDni(dni)
        print(f"{pos.getDni()}   {pos.getNombre()}   {pos.getApellido()}   {pos.getAlias()}   {pos.getPlan()}   {pos.getImporteBasico()}")
        print("ip de conexion      juego     fecha    horaInicio    horaFin")
        for c in self.__arregloConexiones:
            if c.getIdJugador() == pos.getIdJugador():
               print(f"{c.getDireccionIp()}   {c.getNombreDelJuego()}   {c.getFecha()}   {c.getHoraDeInicio()}   {c.getHoraDeFin()}")
               th+= c.getHoraDeFin()-c.getHoraDeInicio()
        print(f"total horas: {th} horas en exceso: {th - pos.getTiempoLimite()}")
        if th > pos.getTiempoLimite():
            if pos.getPlan() == "Basico":
                importe = pos.getImporteBasico() * 1.25
            elif pos.getPlan() == "Completo":
                importe = pos.getImporteBasico() * 1.30
            elif pos.getPlan() == "Extendido":
                importe = pos.getImporteBasico() * 1.40
            print(f"importe: {importe}")
            
    def inciso2(self, juego, gg):
        b= False
        for c in self.__arregloConexiones:
            if c.getNombreDelJuego() == juego:
                print(f"{c.getDireccionIp()}")
                gg.buscarDatos(c)
                b=True
        if b==False:
            raise IndexError("No existe el juego")
        
    def inciso3(self, gg):
        for i in range(len(self.__arregloConexiones)):
            plan = gg.buscarPlan(self.__arregloConexiones[i].getIdJugador())
            if plan:
                for j in range(i+1, len(self.__arregloConexiones)):
                    if self.__arregloConexiones[i] == self.__arregloConexiones[j]:
                        print(f"{self.__arregloConexiones[i].getIdJugador()}")
                        
    def ordenar(self):
        self.__arregloConexiones.sort()