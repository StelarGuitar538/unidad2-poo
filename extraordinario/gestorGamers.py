from gamers import Gamer
import csv

class GestorGamers:
    __gestorGamers = list
    
    def __init__(self):
        self.__gestorGamers = []
        
        
    def inicializar(self):
        archivo = open("C:/Users/danie/OneDrive/Documentos/GitHub/unidad2-poo/extraordinario/archivoscsv/gammers.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            g = Gamer(int(fila[0]), fila[1], fila[2], fila[3], fila[4], fila[5], int(fila[6]), int(fila[7]))
            self.__gestorGamers.append(g)
        archivo.close()
        
    def mostrar(self):
        for g in self.__gestorGamers:
            print(g)
            
    def buscarDNI(self, gc, dni):
        i=0
        while i < len(self.__gestorGamers) and self.__gestorGamers[i].getDni() != dni:
            i+=1
        if i<len(self.__gestorGamers):
            print("existe el jugador")
            print(f" DNI: {self.__gestorGamers[i].getDni()}     nombre y apellido: {self.__gestorGamers[i].getNombre()} {self.__gestorGamers[i].getApellido()}")
            print(f" alias: {self.__gestorGamers[i].getAlias()}     plan: {self.__gestorGamers[i].getPlan()}     importe base: {self.__gestorGamers[i].getImporteBase()}")
            gc.buscarConexion(self.__gestorGamers[i])
        else:
            print("no existe")
            
            
    def buscarDatos(self, dato):
        for g in self.__gestorGamers:
            if g.getIdJugador() == dato.getIdJugador():
                print(f"{g.getNombre()} {g.getApellido()} {g.getAlias()} {g.getPlan()}")
   
    def buscarIdJugador(self, id):
        i=0
        while i < len(self.__gestorGamers) and self.__gestorGamers[i].getIdJugador() != id:
            i+=1
        if i<len(self.__gestorGamers):
            if self.__gestorGamers[i].getPlan() == "Basico":
                dato= self.__gestorGamers[i].getIdJugador()
                return dato