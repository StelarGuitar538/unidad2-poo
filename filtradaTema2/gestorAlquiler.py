from alquiler import Alquiler
import csv

class GestorAlquiler:
    __gestorAlquiler = list
    
    def __init__(self):
        self.__gestorAlquiler = []
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/u2 poo/filtradaTema2/archivoscsv/Alquiler.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            alq = Alquiler(fila[0], fila[1], int(fila[2]), int(fila[3]), int(fila[4]))
            self.__gestorAlquiler.append(alq)
        archivo.close()
        
    def mostrar(self):
        for alq in self.__gestorAlquiler:
            print(alq)
            
    def ordenar(self):
        self.__gestorAlquiler.sort()
        
    def horas(self, alq):
        hora = int(alq.getMinutosTotales()) / 60
        return hora

    
    def listado(self, gv):
        importeTotal = 0
        print("hora:  id de cancha:    duracion alquiler  importe por hora  importe alquiler")
        for alq in self.__gestorAlquiler:
            duracion = self.horas(alq)
            importePorHora = gv.buscarCancha(alq.getIdCanchaAlquilada())
            importeAlquiler = duracion * importePorHora
            importeTotal += importeAlquiler
            print(f"{alq.getHoraAlquilada()}:  {alq.getIdCanchaAlquilada()}:  {duracion}  {importePorHora}  {importeAlquiler}")
        print(f"Total: {importeTotal}")
            
    def mostrarMinutosAlquilada(self):
        id = input("ingrese id de cancha: ")
        min = 0
        for alq in self.__gestorAlquiler:
            if alq.getIdCanchaAlquilada() == id:
                min += int(alq.getMinutosTotales())
        print(f"Minutos alquilados: {min}")