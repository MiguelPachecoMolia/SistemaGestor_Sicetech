from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, estado, municipio, colonia, calle, telefono, correo):
        self.nombre = nombre
        self.estado = estado
        self.municipio = municipio
        self.colonia = colonia
        self.calle = calle
        self.telefono = telefono
        self.correo = correo