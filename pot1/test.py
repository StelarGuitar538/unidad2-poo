from gestorMovimientos import GestorMovimientos
from gestorClientes import GestorClientes

def test():
    gm = GestorMovimientos()
    gc = GestorClientes()
    
    b=False
    while not b:
        print("0, carga")
        print("1, saldo actualizado")
        print("2, buscar cliente")

        
        op = input("ingrese opcion: ")
        if op == "0":
            gm.inicializar()
            gc.inicializar()
            gm.ordenar()
            gm.mostrar()
            gc.mostrar()
        
        elif op == "1":
            gc.listado(gm)
            
        elif op == "2":
            gc.buscarCliente(gm)
        
        else:
            b=True
if __name__ == "__main__":
    test()