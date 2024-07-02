from clases.tecnico_class import Tecnico
from clases.ayudanteGeneral_class import AyudanteGeneral
from utils import clear_screen, get_next_id
from database import get_db, close_connection

def menu_empleados():
    db, client = get_db()  # Abrimos la conexión con la bd
    while True:
        clear_screen()
        print("\n == MENU EMPLEADOS == \n")
        print("1.- Consultar todos los empleados")
        print("2.- Eliminar un empleado")
        print("3.- Registrar un nuevo técnico")
        print("4.- Registrar un nuevo ayudante general")
        print("5.- Volver al menú principal")
        opcion = input("\nOpción deseada: ")
        
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 5:
                if opcion == 1:
                    clear_screen()
                    all_empleados(db)
                elif opcion == 2:
                    eliminar_empleado(db)
                elif opcion == 3:
                    registrar_nuevo_tecnico(db)
                elif opcion == 4:
                    registrar_nuevo_ayudante_general(db)
                elif opcion == 5:
                    close_connection()
                    input("\n\nConexión cerrada. Presiona Enter para salir de Empleados.")
                    break
            else:
                print("\n\nOpción no disponible!!!\n")
        else:
            print("\n\nPor favor, ingresa un número válido!!!\n")
        

def all_empleados(db):
    print("\n == Todos los Empleados ==\n")
    coleccion_empleados = db.empleados
    cursor = coleccion_empleados.find()
    empleados_vacio = True
    
    # Mostramos los empleados
    for empleado in cursor:
        print(f"ID: {empleado['_id']}")
        print(f"Nombre: {empleado['nombre']}")
        print(f"Tipo: {'Técnico' if 'especializacion' in empleado else 'Ayudante General'}")
        print(f"Dirección: {empleado['estado']}, {empleado['municipio']}, {empleado['colonia']}, {empleado['calle']}")
        print(f"Teléfono: {empleado['telefono']}")
        print(f"Correo: {empleado['correo']}")
        print(f"Fecha Registro: {empleado['fecha_registro']}")
        print(f"Servicios: {empleado['servicios']}")
        print("------------------------")
        empleados_vacio = False
        
    if empleados_vacio:
        print("\nNo hay empleados registrados.")
        
    input("\n\nPresiona Enter para continuar...")
    

def eliminar_empleado(db):
    clear_screen()
    all_empleados(db)
    print("\n == Eliminar Empleado == \n")
    id_empleado = input("Ingrese el ID del empleado a eliminar: ")

    try:
        id_empleado = int(id_empleado)  # Convierte a entero si el ID es de tipo entero
    except ValueError:
        print("\nID inválido. Por favor, ingrese un número entero válido.")
        input("\nPresiona Enter para continuar...")
        return

    coleccion_empleados = db.empleados
    resultado = coleccion_empleados.delete_one({"_id": id_empleado})

    if resultado.deleted_count > 0:
        print(f"\nEmpleado con ID {id_empleado} eliminado exitosamente.")
    else:
        print(f"\nNo se encontró ningún empleado con ID {id_empleado}. Intente nuevamente.")

    input("\nPresiona Enter para continuar...")


def registrar_nuevo_tecnico(db):
    clear_screen()
    print("\n == Nuevo Técnico ==\n")
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    correo = input("Correo: ").strip()
    estado = input("Dirección (Estado): ").strip().title()
    municipio = input("Municipio: ").strip().title()
    colonia = input("Colonia: ").strip().title()
    calle = input("Calle: ").strip()
    especializacion = input("Especialización: ").strip().title()
    
    # Generamos el nuevo id
    nuevo_id = get_next_id("empleado_id", db)
    
    # Objeto técnico
    nuevo_tecnico = Tecnico(nombre, estado, municipio, colonia, calle, telefono, correo, nuevo_id, especializacion)
    tecnico_dict = nuevo_tecnico.to_dict()
    
    # Insertamos el técnico en la bd
    coleccion_empleados = db.empleados
    coleccion_empleados.insert_one(tecnico_dict)
    
    print("\nTécnico insertado con ID:", nuevo_id)
    input("\nPresiona Enter para continuar...")


def registrar_nuevo_ayudante_general(db):
    clear_screen()
    print("\n == Nuevo Ayudante General ==\n")
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    correo = input("Correo: ").strip()
    estado = input("Dirección (Estado): ").strip().title()
    municipio = input("Municipio: ").strip().title()
    colonia = input("Colonia: ").strip().title()
    calle = input("Calle: ").strip()
    sueldo_semanal = float(input("Sueldo Semanal: ").strip())
    
    # Generamos el nuevo id
    nuevo_id = get_next_id("empleado_id", db)
    
    # Objeto ayudante general
    nuevo_ayudante = AyudanteGeneral(nombre, estado, municipio, colonia, calle, telefono, correo, nuevo_id, sueldo_semanal)
    ayudante_dict = nuevo_ayudante.to_dict()
    
    # Insertamos el ayudante general en la bd
    coleccion_empleados = db.empleados
    coleccion_empleados.insert_one(ayudante_dict)
    
    print("\nAyudante General insertado con ID:", nuevo_id)
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    menu_empleados()
