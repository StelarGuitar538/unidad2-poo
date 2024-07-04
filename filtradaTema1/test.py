from gestorReserva import GestorReserva
from gestorCabana import GestorCabana

def test():
    gr = GestorReserva()
    gc = GestorCabana()
    
    b=False
    while not b:
        print("0, carga")
        print("1, listado")
        print("2, mostrar cabanas")

        
        op = input("ingrese opcion: ")
        if op == "0":
            gr.inicializar()
            gc.inicializar()
            gr.mostrar()
            gc.mostrar()
        
        elif op == "1":
            gc.buscarCabana()
            
        elif op == "2":
            gr.puntob(gc)
            
        else:
            b=True
if __name__ == "__main__":
    test()