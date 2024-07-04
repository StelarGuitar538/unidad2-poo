from gestorAlquiler import GestorAlquiler
from gestorCancha import GestorCancha

def test():
    ga = GestorAlquiler()
    gc = GestorCancha()
    
    b=False
    while not b:
        print("0, carga")
        print("1, listado")
        print("2, mostrar canchas")
        
        op = input("ingrese opcion: ")
        if op == "0":
            ga.inicializar()
            gc.inicializar()
            ga.ordenar()
            ga.mostrar()
            gc.mostrar()
        
        elif op == "1":
            ga.listado(gc)
            
        elif op == "2":
            ga.mostrarMinutosAlquilada()
        
        else:
            b=True
if __name__ == "__main__":
    test()