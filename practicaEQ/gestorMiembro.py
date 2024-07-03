from claseMiembro import Miembro
import csv
import numpy as np

class GestorMiembro:
    __arregloMiembros = np.ndarray
    __cantidad = 0
    __dimension = 0
    __incremento = 1
    
    def __init__(self):
        self.__arregloMiembros = np.empty([0], dtype=Miembro)
        
    def agregar(self, m):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__arregloMiembros.resize(self.__dimension)
        self.__arregloMiembros[self.__cantidad] = m
        self.__cantidad += 1
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/u2 poo/practicaEQ/archivoscsv/Miembros.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nm = Miembro(fila[0], fila[1], fila[2])
            self.agregar(nm)
        archivo.close()
        
    def mostrar(self):
        for m in self.__arregloMiembros:
            print(m)
            
            
    def buscarMiembro(self, mail):
        b= False
        i=0
        while not b and i< len(self.__arregloMiembros):
                if self.__arregloMiembros[i].getMail() == mail:
                    b= True
                else: i+=1
        return self.__arregloMiembros[i]
    
    def puntoa(self, gv):
        mail = input("ingrese mail: ")
        m = self.buscarMiembro(mail)
        tm = gv.buscarVisualizacion(m)
        print(f"total minutos: {tm}")
        

    def puntob(self, gv):
        for miembro in self.__arregloMiembros:
            aux = miembro.getId()
            if gv.visualizacionessimultaneas(aux):
                print(f"{miembro.getId()} {miembro.getNya()} {miembro.getMail()}")