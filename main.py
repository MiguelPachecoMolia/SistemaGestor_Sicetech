from utils import clear_screen
from menu.clientes import menu_clientes
from menu.servicios import menu_servicios
from menu.empleados import menu_empleados
from menu.analisis import menu_analisis

def main():
    clear_screen()
    print("\n == SICETECH == \n")
    print("\n BIENVENIDO")
    clear_screen()
    menu()

def menu():
    while True:
        print("\n == MENU == \n")
        print("1.- Servicios")
        print("2.- Empleados")
        print("3.- Clientes")
        print("4.- Inventario")
        print("5.- Análisis")
        print("6.- Salir")
        
        opcion = input("\nOpción deseada: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 6:
                clear_screen()
                if opcion == 1:
                    menu_servicios()
                    pass
                elif opcion == 2:
                    menu_empleados()
                    pass
                elif opcion == 3:
                    menu_clientes()
                elif opcion == 4:
                    #inventario.menu_inventario()
                    pass
                elif opcion == 5:
                    menu_analisis()
                    pass
                elif opcion == 6:
                    print("Gracias por usar SICETECH. ¡Adiós!")
                    break
            else:
                print("\n\nOpción No Disponible!!!!\n")
        else:
            print("\n\nPor favor, ingresa un número válido!!!\n")
        clear_screen()

if __name__ == '__main__':
    main()
