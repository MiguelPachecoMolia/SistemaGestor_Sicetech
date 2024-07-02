from clases.cliente_class import Cliente
from utils import clear_screen, get_next_id
from database import get_db, close_connection

def menu_clientes():
    
    db, client = get_db()  #Abrimos la conexion con la bd
    while True:
        clear_screen()
        print("\n == MENU CLIENTES == \n")
        print("1.- Consultar todos los clientes")
        print("2.- Eliminar un cliente")
        print("3.- Registrar un nuevo cliente")
        print("4.- Volver al menú principal")
        opcion = input("\nOpcion deseada: ")
        
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 4:
                if opcion == 1:
                    clear_screen()
                    all_clientes(db)
                elif opcion == 2:
                    eliminar_cliente(db)
                elif opcion == 3:
                    registrar_nuevo_cliente(db)
                elif opcion == 4:
                    close_connection()
                    input("\n\nConexion cerrada. Presiona Enter para Salir de Clientes!!")
                    break
            else:
                print("\n\nOpción No Disponible!!!\n")
        else:
            print("\n\nPor favor, ingresa un número válido!!!\n")
        
        
        
def all_clientes(db):
    print("\n == Todos los Clientes ==\n")
    coleccion_clientes = db.clientes
    cursor = coleccion_clientes.find()
    clientes_vacio = True
    
    #Mostramos los clientes
    for cliente in cursor:
        print(f"ID: {cliente['_id']}")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Dirección: {cliente['estado']}, {cliente['colonia']}, {cliente['calle']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Correo: {cliente['correo']}")
        print(f"Fecha Registro: {cliente['fecha_registro']}")
        print(f"Servicios: {cliente['servicios']}")
        print("------------------------")
        clientes_vacio = False
        
    if clientes_vacio == True:
        print("\nNo hay clientes registrados")
        
    input("\n\n¡¡Presiona Enter para continuar!!")
        
        
    
def eliminar_cliente(db):
    clear_screen()
    all_clientes(db)
    print("\n == Eliminar cliente == \n")
    id_cliente = input("Ingrese el ID del cliente a eliminar: ")

    try:
        id_cliente = int(id_cliente)  # Convierte a entero si el ID es de tipo entero
    except ValueError:
        print("\nID inválido. Por favor, ingrese un número entero válido.")
        input("\nPresiona Enter para continuar...")
        return

    coleccion_clientes = db.clientes
    resultado = coleccion_clientes.delete_one({"_id": id_cliente})

    if resultado.deleted_count > 0:
        print(f"\nCliente con ID {id_cliente} eliminado exitosamente.")
    else:
        print(f"\nNo se encontró ningún cliente con ID {id_cliente}. Intente nuevamente.")

    input("\nPresiona Enter para continuar...")
    

def registrar_nuevo_cliente(db):
    clear_screen()
    print("\n == Nuevo Cliente ==\n")
    nombre = input("Nombre: ").strip()
    telefono = input("Telefono: ").strip()
    correo = input("Correo: ").strip()
    estado = input("Direccion(Estado): ").strip().title()
    municipio = input("Municipio: ").strip().title()
    colonia = input("Colonia: ").strip().title()
    calle = input("Calle: ").strip()
    
    #Generamos el nuevo id
    nuevo_id = get_next_id("cliente_id", db)
    
    #Objeto cliente
    new_cliente = Cliente(nombre, estado, municipio, colonia, calle, telefono, correo, nuevo_id)
    cliente_dict = new_cliente.to_dict()
    
    #Insertamos el cliente a la bd
    coleccion_clientes = db.clientes
    coleccion_clientes.insert_one(cliente_dict)
    print("\nEmpleado insertado con ID: ",nuevo_id)
    input("\nPresiona Enter para continuar...")