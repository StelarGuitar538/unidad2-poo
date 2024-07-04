from maquinaria import Maquinaria
from herramientas import Herramientas
from nodo import Nodo
import csv

class lista:
    __comienzo: Nodo

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
 
 
    def agregar(self, v):  
        nodo = Nodo(v)
        nodo.setSig(self.__comienzo)
        self.__comienzo = nodo
        
    def inicializar(self):
        archivo = open("unidad3/parcial2/archivoCSV/equipos.csv")  
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if fila[0] == "M":
                maquinaria1 = Maquinaria(fila[1], fila[2], int(fila[3]), (fila[4]), (fila[5]), int(fila[6]),float(fila[7]), int(fila[8]), fila[9], int(fila[10]))
                self.agregar(maquinaria1)
            elif fila[0] == "E":
                herramientas1 = Herramientas(fila[1], fila[2], int(fila[3]), (fila[4]), (fila[5]), (fila[6]), float(fila[7]), int(fila[8]), fila[9])
                self.agregar(herramientas1)
        
        
    def mostrarL(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getEquipo())
            aux = aux.getSig()
            
    def mostrarL2(self, pos):
        aux = self.__comienzo
        i=0
        while aux != None and i < pos:
            aux = aux.getSig()
            i+=1
        if aux != None:
            equipo = aux.getEquipo()
            if isinstance(equipo, Maquinaria):
                print(f"La posicion {pos} es una maquinaria")
            elif isinstance(equipo, Herramientas):
                print(f"La posicion {pos} es una herramienta")
        else:
            raise IndexError("No existe la posicion")


    def cantiHerramientas(self, a):
        ca = 0
        aux = self.__comienzo
        while aux != None:
            equipo = aux.getEquipo()
            if isinstance(equipo, Herramientas) and a == equipo.getAnoFabricaion():
                ca +=1
            aux = aux.getSig()
        print(f"la cantidad de herramientas es {ca}")
        
        
    def capacidadCarga(self, a):
        ca = 0
        aux = self.__comienzo
        while aux != None:
            equipo = aux.getEquipo()
            if isinstance(equipo, Maquinaria) and a <= equipo.getCapacidadDeCarga():
                ca +=1
            aux = aux.getSig()
        print(f"la cantidad de maquinarias es {ca}")
        
        
    def mostrar4(self):
        aux = self.__comienzo
        while aux != None:
            equipo = aux.getEquipo()
            print(f"{equipo.getMarca()}, {equipo.getModelo()}, {equipo.getAnoFabricaion()}, {equipo.getTipoCombustible()}, {equipo.getPotencia()}, {equipo.getCapacidadDeCarga()}, {equipo.tarifaAlquiler()}")
            aux = aux.getSig()