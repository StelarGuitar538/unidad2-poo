from cancha import Cancha
import csv
import numpy as np

class GestorCancha:
    __arregloCanchas = np.ndarray
    __cantidad = 0
    __dimension = 0
    __incremento = 1
    
    def __init__(self):
        self.__arregloCanchas = np.empty([0], dtype=Cancha)
        
    def agregar(self, c):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__arregloCanchas.resize(self.__dimension)
        self.__arregloCanchas[self.__cantidad] = c
        self.__cantidad += 1
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/u2 poo/filtradaTema2/archivoscsv/Canchas.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            c = Cancha(fila[0], fila[1], float(fila[2]))
            self.agregar(c)
        archivo.close()
        
    def mostrar(self):
        for c in self.__arregloCanchas:
            print(c)
            
    def buscarCancha(self, id):
        i=0
        while i < self.__cantidad and self.__arregloCanchas[i].getId() != id:
            i += 1
        if i< self.__cantidad:
            return self.__arregloCanchas[i].getImportePorHora()
        else:
            print("No existe la cancha")