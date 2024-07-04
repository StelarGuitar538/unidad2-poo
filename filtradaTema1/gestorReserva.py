from reserva import Reserva
import csv

class GestorReserva:
    __reservas = list
    
    def __init__(self):
        self.__reservas = []
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/u2 poo/filtradaTema1/archivoscsv/Reservas.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            r = Reserva(int(fila[0]), fila[1], int(fila[2]), fila[3], int(fila[4]), int(fila[5]), float(fila[6]))
            self.__reservas.append(r)
        archivo.close()
        
    def mostrar(self):
        for r in self.__reservas:
            print(r)
            
    def puntob(self, gc):
        fecha = input("ingrese fecha: ")
        for r in self.__reservas:
            cd = int(r.getCantidadDias())
            importDiario = float(gc.buscarImportePorDia(r.getNumeroCabana()))
            sena = int(r.getSena())
            importeTotal = importDiario * cd - sena
            if r.getFechaInicio() == fecha:
                print(f"{r.getNumeroCabana()} {importDiario} {cd} {sena} {importeTotal}")