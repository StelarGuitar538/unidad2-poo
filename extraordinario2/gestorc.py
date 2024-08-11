from conexiones import Conexiones
import csv
import numpy as np

class GestorC:
    __arregloConexiones: np.ndarray
    __cantidad: int
    __dimension: int
    __incremento: int
    
    def __init__(self):
        self.__arregloConexiones = np.empty([0], dtype=Conexiones)
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 1
        
    def agregar(self, conexion):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__arregloConexiones.resize((self.__dimension))
        self.__arregloConexiones[self.__cantidad] = conexion
        self.__cantidad += 1
        
    def inicializar(self):
        archivo = open("C:/Users/danie/OneDrive/Documentos/GitHub/unidad2-poo/extraordinario2/archivoscsv/conexiones.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for row in reader:
            self.agregar(Conexiones(int(row[0]), row[1], row[2], row[3], int(row[4]), int(row[5])))
        archivo.close()
        
    def mostrar(self):
        for conexion in self.__arregloConexiones:
            print(conexion)
    
    def inciso1(self, dato):
        hi=0
        hf=0
        print("id ip nombrejuego fecha horaInicio horaFin")
        for conexion in self.__arregloConexiones:
            if conexion.getId() == dato.getId():
                print(conexion)
                hi += conexion.getHoraInicio()
                hf += conexion.getHoraFin()
        total = hi + hf
        exceso = total - dato.getTiempoLimite()
        print(f"total: {total} exceso: {exceso}")
        if total > dato.getTiempoLimite():
            if dato.getPlan() == "Basico":
                importe = dato.getImporteBase() * 1.25
            elif dato.getPlan() == "Completo":
                importe = dato.getImporteBase() * 1.30
            elif dato.getPlan() == "Extendido":
                importe = dato.getImporteBase() * 1.40
            print(f"importe: {importe}")
                
    def inciso2(self, juego, gg):
        b= False
        
        for conexion in self.__arregloConexiones:
            if conexion.getNombreJuego() == juego:
                print(f"{conexion.getIp()}")
                gg.buscarDatos(conexion)
                b=True
        if b==False:
            print("el juego no existe")
            
    def inciso3(self, gg):
        for i in range(len(self.__arregloConexiones)):
            dato = gg.buscarIdJugador(self.__arregloConexiones[i].getId())
            if dato:
                for j in range(i+1, len(self.__arregloConexiones)):
                    if self.__arregloConexiones[i] == self.__arregloConexiones[j]:
                        print(f"{self.__arregloConexiones[i].getId()}")
    
    def ordenar(self):
        return self.__arregloConexiones.sort()