from clases.empleado_class import Empleado

class AyudanteGeneral(Empleado):
    def __init__(self, nombre, estado, municipio, colonia, calle, telefono, correo, id_empleado, sueldo_semanal):
        super().__init__(nombre, estado, municipio, colonia, calle, telefono, correo, id_empleado)
        self.sueldo_semanal = sueldo_semanal

        
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
            'sueldo_semanal': self.sueldo_semanal,
            'servicios': self.servicios
        }