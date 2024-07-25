from gamers import Gamer
import csv

class GestorGamers:
    __gestor = list
    
    
    def __init__(self):
        self.__gestor = []
        
    
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/u2 poo/extraordinario1/archivoscsv/gammers.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            g = Gamer(int(fila[0]), fila[1], fila[2], fila[3], fila[4], fila[5], float(fila[6]), int(fila[7]))
            self.__gestor.append(g)
        archivo.close()
        
    def mostrar(self):
        for g in self.__gestor:
            print(g)
            
            
    def buscarDni(self, dni):
        i=0
        while i < len(self.__gestor) and self.__gestor[i].getDni() != dni:
            i+=1
            
        if i < len(self.__gestor):
            return self.__gestor[i]
        else:
            raise IndexError("No existe el jugador")
        
    def buscarDatos(self, c):
        for g in self.__gestor:
            if g.getIdJugador() == c.getIdJugador():
                print(f"{g.getNombre()} {g.getApellido()} {g.getAlias()} {g.getPlan()}")
                
                
    def buscarPlan(self, idJugador):
        i=0
        while i < len(self.__gestor) and self.__gestor[i].getIdJugador() != idJugador:
            i+=1
            
        if i < len(self.__gestor) and self.__gestor[i].getPlan() == "Basico":
            return True
        else:
            return False