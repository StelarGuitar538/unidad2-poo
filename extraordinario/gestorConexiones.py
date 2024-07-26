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
        
    def agregar(self, c):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__arregloConexiones.resize(self.__dimension)
        self.__arregloConexiones[self.__cantidad] = c
        self.__cantidad += 1
        
    def inicializar(self):
        archivo = open("C:/Users/danie/OneDrive/Documentos/GitHub/unidad2-poo/extraordinario/archivoscsv/conexiones.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            c = Conexion(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
            self.agregar(c)
        archivo.close()
        
    def mostrar(self):
        for c in self.__arregloConexiones:
            print(c)
            
    def buscarConexion(self, dato):
        ci = 0
        cf = 0
        importe = 0
        print("ip de la conexion, nombre del juego, fecha, hora inicio, hora fin")
        for c in self.__arregloConexiones:
            if c.getIdJugador() == dato.getIdJugador():
                print(f"{c.getDireccionIp()} {c.getNombreJuego()} {c.getFechaJuego()} {c.getHoraInicio()} {c.getHoraFin()}")
                ci += c.getHoraInicio()
                cf += c.getHoraFin()
        horas = cf - ci
        horasExceso = horas - dato.getTiempoLimite()
        print(f"horas: {horas} horas exceso: {horasExceso}")
        if horas > dato.getTiempoLimite():
            if dato.getPlan() == "Basico":
                importe = dato.getImporteBase() * 1.25
            elif dato.getPlan() == "Completo":
                importe = dato.getImporteBase() * 1.30
            elif dato.getPlan() == "Extendido":
                importe = dato.getImporteBase() * 1.40
        print(f"importe: {importe}")
        
    def buscarJuego(self, juego, g):
        bandera=False
        for c in self.__arregloConexiones:
            if c.getNombreJuego() == juego:
                print(f"{c.getDireccionIp()}")
                g.buscarDatos(c)
                bandera=True
        if bandera==False:
            print("el juego no existe")
                
    def ordenar(self):
        return self.__arregloConexiones.sort()
        
          
    def comparar(self, g):
        for i in range(len(self.__arregloConexiones)):
            dato = g.buscarIdJugador(self.__arregloConexiones[i].getIdJugador())
            if dato == self.__arregloConexiones[i].getIdJugador():
                for j in range(i+1, len(self.__arregloConexiones)):
                    if self.__arregloConexiones[i] == self.__arregloConexiones[j]:
                        print(f"{self.__arregloConexiones[i].getIdJugador()}")
                                 
    
                
        
        