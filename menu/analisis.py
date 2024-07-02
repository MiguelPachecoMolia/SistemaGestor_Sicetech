from utils import clear_screen, get_next_id
from database import get_db, close_connection

def menu_analisis():
    db, client = get_db()  # Abrimos la conexión con la base de datos
    while True:
        clear_screen()
        print("\n == MENÚ ANÁLISIS == \n")
        print("1.- Análisis de Servicios por Cliente")
        print("2.- Análisis de Costos Totales por Cliente")
        print("3.- Análisis de Servicios por Región")
        print("4.- Volver al menú principal")
        opcion = input("\nOpción deseada: ")
        
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 4:
                if opcion == 1:
                    analisis_servicios_por_cliente(db)
                elif opcion == 2:
                    analisis_costos_totales_por_cliente(db)
                elif opcion == 3:
                    analisis_servicios_por_region(db)
                elif opcion == 4:
                    close_connection()
                    input("\n\nConexión cerrada. Presiona Enter para volver al menú principal.")
                    break
            else:
                print("\n\nOpción No Disponible!!!\n")
        else:
            print("\n\nPor favor, ingresa un número válido!!!\n")
            
            
            
def analisis_servicios_por_cliente(db):
    coleccion_servicios = db.servicios
    coleccion_clientes = db.clientes
    
    pipeline = [
        {"$group": {"_id": "$id_cliente", "total_servicios": {"$sum": 1}}},
        {"$sort": {"total_servicios": -1}}
    ]
    
    resultados = list(coleccion_servicios.aggregate(pipeline))
    
    clear_screen()
    print("\n == Análisis de Servicios por Cliente ==\n")
    
    if resultados:
        for resultado in resultados:
            cliente_id = resultado["_id"]
            total_servicios = resultado["total_servicios"]
            
            cliente = coleccion_clientes.find_one({"_id": cliente_id})
            nombre_cliente = cliente["nombre"] if cliente else "Cliente desconocido"
            
            print(f"ID Cliente: {cliente_id}")
            print(f"Nombre Cliente: {nombre_cliente}")
            print(f"Total Servicios: {total_servicios}")
            print("------------------------")
    else:
        print("\nNo se encontraron servicios.")
    
    input("\nPresiona Enter para continuar...")
    
    
    
def analisis_costos_totales_por_cliente(db):
    coleccion_servicios = db.servicios
    coleccion_clientes = db.clientes
    
    pipeline = [
        {"$group": {"_id": "$id_cliente", "costo_total": {"$sum": "$costo_total"}}},
        {"$sort": {"costo_total": -1}}
    ]
    
    resultados = list(coleccion_servicios.aggregate(pipeline))
    
    clear_screen()
    print("\n == Análisis de Costos Totales por Cliente ==\n")
    
    if resultados:
        for resultado in resultados:
            cliente_id = resultado["_id"]
            costo_total = resultado["costo_total"]
            
            cliente = coleccion_clientes.find_one({"_id": cliente_id})
            nombre_cliente = cliente["nombre"] if cliente else "Cliente desconocido"
            
            print(f"ID Cliente: {cliente_id}")
            print(f"Nombre Cliente: {nombre_cliente}")
            print(f"Costo Total: {costo_total}")
            print("------------------------")
    else:
        print("\nNo se encontraron servicios.")
    
    input("\nPresiona Enter para continuar...")
    
# ======= ANALISIS POR REGIONES ======= 
    
def analisis_servicios_por_region(db):
    while True:
        clear_screen()
        print("\n == Análisis de Servicios por Región ==\n")
        print("1.- Por Estado")
        print("2.- Por Municipio")
        print("3.- Por Colonia")
        print("4.- Volver al menú de Analisis")
        opcion = input("\nElige el nivel de análisis: ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 4:
                if opcion == 1:
                    analisis_por_estado(db)
                elif opcion == 2:
                    analisis_por_municipio(db)
                elif opcion == 3:
                    analisis_por_colonia(db)
                elif opcion == 4:
                    break    
            else:
                print("\n\nOpción No Disponible!!!\n")
        else:
            print("\n\nPor favor, ingresa un número válido!!!\n")
    
    
def analisis_por_estado(db):
    clear_screen()
    print("\n == Análisis de Servicios por Estado ==\n")
    pipeline = [
        {"$group": {"_id": {"estado": "$estado"}, "total_servicios": {"$sum": 1}}},
        {"$sort": {"total_servicios": -1}}
    ]
    resultado = db.servicios.aggregate(pipeline)
    for doc in resultado:
        print(f"Estado: {doc['_id']['estado']}")
        print(f"Total Servicios: {doc['total_servicios']}")
        print("------------------------")
    input("\nPresiona Enter para Salir")
        

def analisis_por_municipio(db):
    clear_screen()
    print(f"\n == Análisis de Servicios por Municipio ==\n")
    estado = input("Ingresa el nombre del estado: ").strip().title()
    clear_screen()
    print(f"\n == Análisis de Servicios por Municipio en {estado} ==\n")
    pipeline = [
        {"$match": {"estado": estado}},
        {"$group": {"_id": {"municipio": "$municipio"}, "total_servicios": {"$sum": 1}}},
        {"$sort": {"total_servicios": -1}}
    ]
    resultado = db.servicios.aggregate(pipeline)
    for doc in resultado:
        print(f"Municipio: {doc['_id']['municipio']}")
        print(f"Total Servicios: {doc['total_servicios']}")
        print("------------------------")
    input("\nPresiona Enter para Salir")

        
def analisis_por_colonia(db):
    clear_screen()
    print(f"\n == Análisis de Servicios por Colonia ==\n")
    estado = input("Ingresa el nombre del estado: ").strip().title()
    municipio = input("Ingresa el nombre del municipio: ").strip().title()
    print(f"Estado: {estado}, Municipio: {municipio}")

    clear_screen()
    print(f"\n == Análisis de Servicios por Colonia en {municipio}, {estado} ==\n")
    pipeline = [
        {"$match": {"estado": estado, "municipio": municipio}},
        {"$group": {"_id": {"colonia": "$colonia"}, "total_servicios": {"$sum": 1}}},
        {"$sort": {"total_servicios": -1}}
    ]
    resultado = db.servicios.aggregate(pipeline)
    for doc in resultado:
        print(f"Colonia: {doc['_id']['colonia']}")
        print(f"Total Servicios: {doc['total_servicios']}")
        print("------------------------")
    input("\nPresiona Enter para Salir")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
Definición del pipeline de agregación:

Utiliza el framework de agregación de MongoDB para agrupar y contar los servicios por región.
El pipeline de agregación tiene dos etapas:
$group: Agrupa los documentos (servicios) por los campos estado, municipio, y colonia y calcula el total de servicios en cada grupo.
$sort: Ordena los resultados por el total de servicios en orden descendente.
'''

