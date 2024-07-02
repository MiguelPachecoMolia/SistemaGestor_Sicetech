from clases.servicio_class import Servicio
from utils import clear_screen, get_next_id
from database import get_db, close_connection

def menu_servicios():
    db, client = get_db()  # Abrimos la conexión con la base de datos
    while True:
        clear_screen()
        print("\n == MENU SERVICIOS == \n")
        print("1.- Consultar todos los servicios")
        print("2.- Registrar un nuevo servicio")
        print("3.- Agregar empleado a un servicio")
        print("4.- Eliminar servicio")
        print("5.- Volver al menú principal")
        opcion = input("\nOpción deseada: ")
        
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 5:
                if opcion == 1:
                    clear_screen()
                    all_servicios(db)
                elif opcion == 2:
                    registrar_nuevo_servicio(db)
                elif opcion == 3:
                    agregar_empleado_a_servicio(db)
                elif opcion == 4:
                    eliminar_servicio(db)
                elif opcion == 5:
                    close_connection()
                    input("\n\nConexión cerrada. Presiona Enter para Salir de Servicios!!")
                    break
            else:
                print("\n\nOpción No Disponible!!!\n")
        else:
            print("\n\nPor favor, ingresa un número válido!!!\n")

def all_servicios(db):
    print("\n == Todos los Servicios ==\n")
    coleccion_servicios = db.servicios
    cursor = coleccion_servicios.find()
    servicios_vacio = True
    
    # Mostramos los servicios
    for servicio in cursor:
        print(f"ID Servicio: {servicio['_id']}")
        print(f"ID Cliente: {servicio['id_cliente']}")
        print(f"Estado: {servicio['estado']}")
        print(f"Municipio: {servicio['municipio']}")
        print(f"Colonia: {servicio['colonia']}")
        print(f"Calle: {servicio['calle']}")
        print(f"Costo Total: ${servicio['costo_total']}")
        print(f"Empleados: {servicio['empleados']}")
        print("------------------------")
        servicios_vacio = False
    
    if servicios_vacio:
        print("\nNo hay servicios registrados.")
    
    input("\n\n¡¡Presiona Enter para continuar!!")

def validar_id_cliente(id_cliente, db):
    coleccion_clientes = db.clientes
    cliente = coleccion_clientes.find_one({"_id": id_cliente})
    return cliente is not None

def registrar_nuevo_servicio(db):
    while True:
        clear_screen()
        print("\n == Nuevo Servicio ==\n")
        id_cliente = input("ID Cliente: ").strip()

        try:
            id_cliente = int(id_cliente)  # Intenta convertir a entero
        except ValueError:
            print("\nID inválido. Por favor, ingrese un número entero válido.")
            input("\nPresiona Enter para continuar...")
            continue  
            
        coleccion_clientes = db.clientes
        cliente = coleccion_clientes.find_one({"_id": id_cliente})

        if not validar_id_cliente(id_cliente, db):
            print("\n¡El ID del cliente ingresado no existe en la base de datos! Inténtalo nuevamente.")
        else:
            break
    
    estado = input("Estado: ").strip().title()
    municipio = input("Municipio: ").strip().title()
    colonia = input("Colonia: ").strip().title()
    calle = input("Calle: ").strip()
    costo_total = float(input("Costo Total: ").strip())

    # Generamos el nuevo id para el servicio
    nuevo_id = get_next_id("servicio_id", db)
    
    # Creamos el objeto servicio
    nuevo_servicio = Servicio(nuevo_id, id_cliente, estado, municipio, colonia, calle, costo_total)
    servicio_dict = nuevo_servicio.to_dict()

    # Insertamos el servicio en la base de datos
    coleccion_servicios = db.servicios
    coleccion_servicios.insert_one(servicio_dict)
    
    print("\nServicio registrado con ID:", nuevo_servicio.id_servicio)
    
    # Agregamos el ID del servicio al cliente correspondiente
    coleccion_clientes = db.clientes
    coleccion_clientes.update_one(
        {"_id": id_cliente},
        {"$push": {"servicios": nuevo_servicio.id_servicio}}
    )
    
    input("\nPresiona Enter para continuar...")

    
    
def validar_id_empleado(id_empleado, db):
    coleccion_empleados = db.empleados
    empleado = coleccion_empleados.find_one({"_id": id_empleado})
    return empleado is not None

def agregar_empleado_a_servicio(db):
    clear_screen()
    print("\n == Agregar Empleado a Servicio ==\n")
    
    # Mostrar todos los servicios para que el usuario elija uno
    coleccion_servicios = db.servicios
    cursor = coleccion_servicios.find()
    servicios = list(cursor)
    
    if not servicios:
        print("\nNo hay servicios registrados.")
        input("\nPresiona Enter para continuar...")
        return
    
    print("\nServicios Disponibles:")
    for servicio in servicios:
        print(f"ID Servicio: {servicio['_id']}, ID Cliente: {servicio['id_cliente']}")
    
    while True:
        id_servicio = input("\nIngrese el ID del servicio al que desea agregar un empleado: ").strip()

        try:
            id_servicio = int(id_servicio)  # Intenta convertir a entero
        except ValueError:
            print("\nID inválido. Por favor, ingrese un número entero válido.")
            input("\nPresiona Enter para continuar...")
            continue  # Vuelve al inicio del bucle

        servicio = coleccion_servicios.find_one({"_id": id_servicio})
        
        if servicio:
            break
        else:
            print("\n¡ID de servicio no válido! Inténtalo nuevamente.")
    
    while True:
        id_empleado = input("Ingrese el ID del empleado a agregar al servicio: ").strip()
        
        try:
            id_empleado = int(id_empleado)  # Intenta convertir a entero
        except ValueError:
            print("\nID inválido. Por favor, ingrese un número entero válido.")
            input("\nPresiona Enter para continuar...")
            continue 

        if not validar_id_empleado(id_empleado, db):
            print("\n¡El ID del empleado ingresado no existe en la base de datos! Inténtalo nuevamente.")
        else:
            break
    
    # Agregar el ID del empleado al servicio
    coleccion_servicios.update_one(
        {"_id": id_servicio},
        {"$addToSet": {"empleados": id_empleado}}
    )
    
    # Registrar el servicio en la colección de empleados
    coleccion_empleados = db.empleados
    coleccion_empleados.update_one(
        {"_id": id_empleado},
        {"$addToSet": {"servicios": id_servicio}}
    )
    
    print("\n¡Empleado agregado al servicio correctamente!")
    input("\nPresiona Enter para continuar...")

    
    
def eliminar_servicio(db):
    clear_screen()
    print("\n == Eliminar Servicio ==\n")
    
    # Mostrar todos los servicios para que el usuario elija uno
    coleccion_servicios = db.servicios
    cursor = coleccion_servicios.find()
    servicios = list(cursor)
    
    if not servicios:
        print("\nNo hay servicios registrados.")
        input("\nPresiona Enter para continuar...")
        return
    
    print("\nServicios Disponibles:")
    for servicio in servicios:
        print(f"ID Servicio: {servicio['_id']}, ID Cliente: {servicio['id_cliente']}")
    
    while True:
        id_servicio = input("\nIngrese el ID del servicio que desea eliminar: ").strip()
        
        try:
            id_servicio = int(id_servicio)  # Convierte a entero si es posible
        except ValueError:
            print("\nID inválido. Por favor, ingrese un número entero válido.")
            input("\nPresiona Enter para continuar...")
            continue  # Vuelve al inicio del bucle
        
        servicio = coleccion_servicios.find_one({"_id": id_servicio})
        
        if servicio:
            break
        else:
            print("\n¡ID de servicio no válido! Inténtalo nuevamente.")
            input("\nPresiona Enter para continuar...")
    
    # Eliminar el servicio de la colección de servicios
    coleccion_servicios.delete_one({"_id": id_servicio})
    
    # Eliminar el ID del servicio de la lista de servicios de los clientes
    coleccion_clientes = db.clientes
    coleccion_clientes.update_many(
        {"servicios": id_servicio},
        {"$pull": {"servicios": id_servicio}}
    )
    
    # Eliminar el ID del servicio de la lista de servicios de los empleados
    coleccion_empleados = db.empleados
    coleccion_empleados.update_many(
        {"servicios": id_servicio},
        {"$pull": {"servicios": id_servicio}}
    )
    
    print("\n¡Servicio eliminado correctamente!")
    input("\nPresiona Enter para continuar...")
