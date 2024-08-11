from gamers import Gamer
import csv

class GestorG:
    __gamers: list
    
    def __init__(self):
        self.__gamers = []
        
    def inicializar(self):
        archivo = open("C:/Users/danie/OneDrive/Documentos/GitHub/unidad2-poo/extraordinario2/archivoscsv/gammers.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for row in reader:
            self.__gamers.append(Gamer(int(row[0]), int(row[1]), row[2], row[3], row[4], row[5], int(row[6]), int(row[7])))
        archivo.close()
        
    def mostrar(self):
        for gamer in self.__gamers:
            print(gamer)
            
    def inciso1(self, dni, gc):
        i=0
        while i < len(self.__gamers) and self.__gamers[i].getDni() != dni:
            i += 1
        
        if i >= len(self.__gamers):
            print("No existe el jugador")
        else:
            print(self.__gamers[i])
            gc.inciso1(self.__gamers[i])
    
    def buscarDatos(self, dato):
        for gamer in self.__gamers:
            if gamer.getId() == dato.getId():
                print(gamer)
                
    def buscarIdJugador(self, id):
        i=0
        while i < len(self.__gamers) and self.__gamers[i].getId() != id:
            i += 1
        
        if i >= len(self.__gamers):
            return False
        else:
            if self.__gamers[i].getPlan() == "Basico":
               return True
           