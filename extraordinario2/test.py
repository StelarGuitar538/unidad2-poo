from gestorc import GestorC
from gestorG import GestorG

def main():
    gc = GestorC()
    gg = GestorG()
    
    b= False
    
    while not b:
        print("0. carga \n 1. inciso1 \n 2. inciso2 \n 3. inciso3 \n 4. salida")
        
        opcion = int(input("Opcion: "))
        
        if opcion == 0:
            gc.inicializar()
            gg.inicializar()
            gc.ordenar()
            gc.mostrar()
            gg.mostrar()
            
        elif opcion == 1:
            try:
                dni = int(input("DNI: "))
                gg.inciso1(dni, gc)
            except ValueError:
                print("El DNI ingresado no es valido")
        
        elif opcion == 2:
            juego = input("Juego: ")
            gc.inciso2(juego, gg)
        
        elif opcion == 3:
            gc.inciso3(gg)
        
        elif opcion == 4:
            b = True


if __name__ == "__main__":
    main()