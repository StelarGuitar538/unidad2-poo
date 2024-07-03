from gestorMiembro import GestorMiembro
from gestorVisualizacion import GestorVisualizacion

def test():
    gm = GestorMiembro()
    gv = GestorVisualizacion()
    
    b=False
    while not b:
        print("0, carga")
        print("1, mostrar miembros")
        print("2, mostrar visualizaciones")
        
        op = input("ingrese opcion: ")
        if op == "0":
            gm.inicializar()
            gv.inicializar()
            gm.mostrar()
            gv.mostrar()
        
        elif op == "1":
            gm.puntoa(gv)
        
        elif op == "2":
            gm.puntob(gv)
        else:
            b=True
if __name__ == "__main__":
    test()