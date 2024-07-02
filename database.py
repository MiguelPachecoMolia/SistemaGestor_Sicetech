#Archivo db.py

from pymongo import MongoClient

# Definimos una variable global para almacenar la conexión de cliente
# Esto nos permite reutilizar la misma conexión en todo el programa
# y cerrarla adecuadamente al finalizar.
global_client = None

def get_db():
    global global_client

    if global_client is None:
        # Si no hay una conexión activa, creamos una nueva
        global_client = MongoClient('mongodb://localhost:27017')

    # Devolvemos tanto la base de datos como el cliente
    db = global_client['sicetech']
    return db, global_client

def close_connection():
    global global_client

    if global_client is not None:
        # Cerramos la conexión del cliente si está abierta
        global_client.close()
        global_client = None  # Resetamos la variable global al cerrar la conexión


"""
from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://localhost:27017')
    db = client['sicetech']
    return db, client
    
"""    