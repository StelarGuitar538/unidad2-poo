from mama import Mama
import csv
import numpy as np

class GestorMama:
    __arregloMamas = np.ndarray
    __cantidad = 0
    __dimension = 0
    __incremento = 1
    
    def __init__(self):
        self.__arregloMamas = np.empty([0], dtype=Mama)
        
    def agregar(self, m):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__arregloMamas.resize(self.__dimension)
        self.__arregloMamas[self.__cantidad] = m
        self.__cantidad += 1
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/u2 poo/practicaEQT1/archivoscsv/Mamas.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            m = Mama((fila[0]), int(fila[1]), fila[2])
            self.agregar(m)
        archivo.close()
        
    def mostrar(self):
        for m in self.__arregloMamas:
            print(m)

    
    def listado(self, gn, dni):
        i=0
        while (dni != self.__arregloMamas[i].getDNI())and(i <= self.__cantidad):
            i+=1
        if(i <= self.__cantidad):
            print(f"{self.__arregloMamas[i].getNya()} \n {self.__arregloMamas[i].getEdad()} \n ")
            gn.buscar(dni)
            
            
    def partosMultiples(self, gn):
        for i in self.__arregloMamas:
            aux = i.getDNI()
            if gn.partos(aux) > 1:
                print(f"{i.getDNI()} \n {i.getNya()} \n {i.getEdad()} cantidad de hijos {gn.partos(aux)}")
                
        
        