from claseVisualizaciones import Visualizacion
import csv

class GestorVisualizacion:
    __arregloVisualizaciones = list
    
    def __init__(self):
        self.__arregloVisualizaciones = []
        
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/u2 poo/practicaEQ/archivoscsv/Visualizaciones.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nm = Visualizacion(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.__arregloVisualizaciones.append(nm)
        archivo.close()
    
    def mostrar(self):
        for v in self.__arregloVisualizaciones:
            print(v)
            
            
    def buscarVisualizacion(self, user):
        totalMinutos = 0
        for i in range(len(self.__arregloVisualizaciones)):
           if self.__arregloVisualizaciones[i].getIdMiembro() == user.getId():
               totalMinutos += int(self.__arregloVisualizaciones[i].getMinutos())
        return totalMinutos
    
    def visualizacionessimultaneas(self, id_miembro):
        i = 0
        long = len(self.__arregloVisualizaciones)
        while i < long and id_miembro != self.__arregloVisualizaciones[i].getIdMiembro():
            i += 1
            
        if i < long:
            a = self.__arregloVisualizaciones[i]
            for j in range(i + 1, long):
                if a == self.__arregloVisualizaciones[j]:
                    return True
        return False
      

    