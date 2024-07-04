from lista import lista
from maquinaria import Maquinaria
from herramientas import Herramientas
from equipos import Equipo

def test():
    l = lista()
    
    
    
    b=False
    
    
    while not b:
        print("1, carga")
        print("2, mostrar posicion")
        print("3, cantidad de herramientas")
        print("4, capacidad de carga")
        print("5, mostrar tarifa de alquiler")
        
        op = input("ingrese opcion: ")
        
        if op == "1":
            l.inicializar()
            l.mostrarL()
            
        elif op == "2":
            pos = int(input("Ingrese posicion: "))
            l.mostrarL2(pos)
            
        
        elif op == "3":
            a = int(input("Ingrese ano de fabricacion: "))
            l.cantiHerramientas(a)
        
        elif op == "4":
            carga = int(input("Ingrese carga: "))
            l.capacidadCarga(carga)
            
        elif op == "5":
            l.mostrar4()
        
        else:
            b=True
            
if __name__ == "__main__":
    test()