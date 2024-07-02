from clases.persona_class import Persona
from datetime import datetime, date

class Empleado(Persona):
    def __init__(self, nombre, estado, municipio, colonia, calle, telefono, correo, id_empleado):
        super().__init__(nombre, estado, municipio, colonia, calle, telefono, correo)
        self.id_empleado = id_empleado
        self.fecha_registro = date.today()
        self.servicios = []
        
    def to_dict(self):
        return {
            '_id': self.id_empleado,
            'nombre': self.nombre,
            'estado': self.estado,
            'municipio': self.municipio,
            'colonia': self.colonia,
            'calle': self.calle,
            'telefono': self.telefono,
            'correo': self.correo,
            'fecha_registro': self.fecha_registro.strftime('%Y-%m-%d'), #Formateo de la fecha
            'servicios': self.servicios
        }