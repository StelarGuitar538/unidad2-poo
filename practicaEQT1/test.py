from gestorMama import GestorMama
from gestorNacimiento import GestorNacimiento

def test():
    gm = GestorMama()
    gn = GestorNacimiento()
    
    b= False
    
    while not b :
        print("0, carga")
        print("1, listado")
        print("2, partos multiples")
    
        op = input("ingrese opcion: ")
        if op == "0":
            gm.inicializar()
            gn.inicializar()
            gm.mostrar()
            gn.mostrar()
            
        elif op == "1":
            dni = int(input("ingrese dni: "))
            gm.listado(gn, dni)
        elif op == "2":
            gm.partosMultiples(gn)
        else:
            b=True
                
if __name__ == "__main__":
    test()
    