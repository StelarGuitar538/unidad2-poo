from gestorConexiones import GestorConexiones
from gestorGamers import GestorGamers

def test():
    gg = GestorGamers()
    gc = GestorConexiones()
    
    b=False
    
    while not b:
        print("""0, carga
1, inciso 1
2, inciso 2
3, inciso 3
4, fin""")
        
        opcion = int(input("opcion: "))
        
        if opcion == 0:
            gg.inicializar()
            gc.inicializar()
            gc.ordenar()
            gg.mostrar()
            gc.mostrar()
            
        elif opcion == 1:
            try:
                dni = input("dni: ")
                gc.inciso1(dni, gg)
            except IndexError as e:
                print(e)
        
        elif opcion == 2:
            try:
                juego = input("nombre del juego: ")
                gc.inciso2(juego, gg)
            except IndexError as e:
                print(e)
                
        elif opcion == 3:
            gc.inciso3(gg)
            
        elif opcion == 4:
            b=True
                
if __name__ == "__main__":
    test()
    