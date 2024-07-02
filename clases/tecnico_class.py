from clases.empleado_class import Empleado

class Tecnico(Empleado):
    def __init__(self, nombre, estado, municipio, colonia, calle, telefono, correo, id_empleado, especializacion):
        super().__init__(nombre, estado, municipio, colonia, calle, telefono, correo, id_empleado)
        self.especializacion = especializacion

        
    def to_dict(self):
        return {
            '_id': self.id_empleado,
            'especializacion': self.especializacion,
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