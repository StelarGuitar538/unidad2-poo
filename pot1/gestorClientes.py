from clientes import Cliente
import csv

class GestorClientes:
    __gestorClientes: list
    
    def __init__(self):
        self.__gestorClientes = []
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/Facultad/poo/unidad2/pot1/archivoscsv/ClientesAbril2024.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            c = Cliente(fila[0], fila[1], fila[2], fila[3], float(fila[4]))
            self.__gestorClientes.append(c)
        archivo.close()
        
    def mostrar(self):
        for c in self.__gestorClientes:
            print(c)
            
    def buscarDni(self, dni):
        b= False
        i=0
        while not b and i< len(self.__gestorClientes):
            if self.__gestorClientes[i].getDni() == dni:
                b= True
                return self.__gestorClientes[i]
            i+=1
        if b is False:
            print("no existe cliente con ese dni")

    def buscarTarjeta(self, numtar):
        b= False
        i=0
        while not b and i< len(self.__gestorClientes):
            if self.__gestorClientes[i].getNumeroTarjeta() == numtar:
                b= True
                return self.__gestorClientes[i]
            i+=1
        if b is False:
            return
        
    def listado(self, gm):
        dni = input("ingrese dni: ")
        nt = self.buscarDni(dni)
        print(f"nombre: {nt.getNombre()} apellido: {nt.getApellido()}                                               numero de tarjeta: {nt.getNumeroTarjeta()}")
        print(f"saldo: {nt.getSaldoAnterior()}")
        print("movimientos \n  fecha  descripcion  tipo de movimiento  importe  ")
        gm.mostrarMovimientos(nt)
        saldo = gm.actualizarSaldo(nt)
        nt.setSaldo(saldo)
        print(f"saldo actualizado: {nt.getSaldoAnterior()}")
        
        
    def buscarCliente(self, gm):
        t = input("ingrese numero de tarjeta")
        numtar = self.buscarTarjeta(t)
        nt = gm.buscarMov(numtar)
        if nt is False:
            print(f" no hay movimientos, apellido: {numtar.getApellido()} nombre: {numtar.getNombre()}")
        else:
            print("si hubieron movimientos")
            