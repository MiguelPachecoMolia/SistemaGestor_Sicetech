#Archvio utils.py

import os
import platform
import time
import pymongo

def clear_screen():
    time.sleep(1.5) #Paussamos el programa antes de limpiar pantalla
    
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
        
def get_next_id(nombre_contador, db):
    counters = db.counters
    counter = counters.find_one_and_update(
        {"_id": nombre_contador},
        {"$inc": {"seq": 1}},
        upsert=True,
        return_document=pymongo.ReturnDocument.AFTER
    )
    return counter["seq"]
