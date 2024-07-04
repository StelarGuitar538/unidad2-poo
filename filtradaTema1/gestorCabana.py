from cabana import Cabana
import csv
import numpy as np

class GestorCabana:
    __arregloCabanas = np.ndarray
    __cantidad = 0
    __dimension = 0
    __incremento = 1
    
    def __init__(self):
        self.__arregloCabanas = np.empty([0], dtype=Cabana)
        
    def agregar(self, c):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__arregloCabanas.resize(self.__dimension)
        self.__arregloCabanas[self.__cantidad] = c
        self.__cantidad += 1
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/u2 poo/filtradaTema1/archivoscsv/Cabanas.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            c = Cabana(fila[0], int(fila[1]), int(fila[2]), int(fila[3]), float(fila[4]))
            self.agregar(c)
        archivo.close()
        
    def mostrar(self):
        for c in self.__arregloCabanas:
            print(c)

    def buscarCabana(self):
        ch = int(input("ingrese cantidad de huespedes: "))
    
        for c in self.__arregloCabanas:
            cap = c.getCantidadDeCamasGrandes() * 2 + c.getCantidadDeCamasPequenas()
            if cap >= ch:
                print(c.getNumero())
                
    def buscarImportePorDia(self, num):
        i=0
        while i < len(self.__arregloCabanas) and self.__arregloCabanas[i].getNumero() == num:
            i+=1
        return self.__arregloCabanas[i].getImportePorDia()    
            
        