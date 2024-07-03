from movimientos import Movimiento
import csv
import numpy as np

class GestorMovimientos:
    __arregloMovimientos = np.ndarray
    __cantidad = 0
    __dimension = 0
    __incremento = 1
    
    def __init__(self):
        self.__arregloMovimientos = np.empty([0], dtype=Movimiento)
        
    def agregar(self, m):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__arregloMovimientos.resize(self.__dimension)
        self.__arregloMovimientos[self.__cantidad] = m
        self.__cantidad += 1
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/Facultad/poo/unidad2/pot1/archivoscsv/MovimientosAbril2024.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nm = Movimiento(fila[0], fila[1], fila[2], fila[3], float(fila[4]))
            self.agregar(nm)
        archivo.close()
        
    def mostrar(self):
        for m in self.__arregloMovimientos:
            print(m)
            
    def actualizarSaldo(self, nt):
        saldo = 0  
        for movimiento in self.__arregloMovimientos:
            if movimiento.getNumeroTarjeta() == nt.getNumeroTarjeta():
                if movimiento.getTipoDeMovimiento() == "P":
                    saldo -= movimiento.getImporte()
                elif movimiento.getTipoDeMovimiento() == "C":
                    saldo += movimiento.getImporte()
        
        return saldo
    
    def mostrarMovimientos(self, nt):
        for movimiento in self.__arregloMovimientos:
            if movimiento.getNumeroTarjeta() == nt.getNumeroTarjeta():
                print(f"{movimiento.getFecha()} {movimiento.getDescripcion()} {movimiento.getTipoDeMovimiento()} {movimiento.getImporte()}")
                
    def buscarMov(self, nt):
        b= False
        i=0
        while not b and i< len(self.__arregloMovimientos):
                if self.__arregloMovimientos[i].getNumeroTarjeta() == nt.getNumeroTarjeta():
                    b= True
                else: i+=1
        return b
    
    def ordenar(self):
        self.__arregloMovimientos.sort()