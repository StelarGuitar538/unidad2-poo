from gestorGamers import GestorGamers
from gestorConexiones import GestorConexiones

def test():
    g = GestorGamers()
    gc = GestorConexiones()
    
    b= False
    
    while not b:
        print("0, carga")
        print("1, punto a")
        print("2, punto b")
        print("3, punto c")
        
        op = int(input("ingrese opcion: "))
        if op == 0:
            g.inicializar()
            gc.inicializar()
            gc.ordenar()
            g.mostrar()
            gc.mostrar()
            
        elif op == 1:
            dni = input("ingrese dni: ")
            g.buscarDNI(gc, dni)
        
        elif op == 2:
            juego = input("ingrese juego: ")
            gc.buscarJuego(juego, g)
            
        elif op == 3:
            gc.comparar(g)
            
        else:
            b=True
            
        
if __name__ == "__main__":
    test()