from nacimiento import Nacimiento
import csv

class GestorNacimiento:
    __nacimientos = list
    
    def __init__(self):
        self.__nacimientos = []
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/u2 poo/practicaEQT1/archivoscsv/Nacimientos.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            n = Nacimiento((fila[0]), fila[1], fila[2], fila[3], (fila[4]), int(fila[5]))
            self.__nacimientos.append(n)
        archivo.close()
        
    def mostrar(self):
        for n in self.__nacimientos:
            print(n)
            
    
    def buscar(self, dni):
        i=0
        b = 0
        for i in range(len(self.__nacimientos)):
            if self.__nacimientos[i].getDNIMama() == dni:
                if b == 0:
                    print(f"tipo de parto {self.__nacimientos[i].getTipoDeParto()}")
                    print(f"bebe/s \n peso:          altura:")
                print(f"{self.__nacimientos[i].getPeso()} \n {self.__nacimientos[i].getAlturaEnCm()}")
                b=1
                
    def partos(self, dni):
        i=0
        c=0
        long = len(self.__nacimientos)
        while i < long and dni != self.__nacimientos[i].getDNIMama():
            i += 1
            
        if i < long:
            pos = self.__nacimientos[i]
            for j in range(i + 1, long):
                if pos == self.__nacimientos[j]:
                    c += 1
        return c