from datetime import datetime, date

class Servicio():
    def __init__(self, id_servicio, id_cliente, estado, municipio, colonia, calle, costo_total):
        today = date.today()
        self.id_servicio = int(f"{today.strftime('%Y%m%d')}{id_servicio}")
        self.id_cliente = id_cliente
        self.estado = estado
        self.municipio = municipio
        self.colonia = colonia
        self.calle = calle
        self.costo_total = costo_total
        self.empleados = []
       
    
    def to_dict(self):
        return {
            '_id': self.id_servicio,
            'id_cliente': self.id_cliente,
            'estado': self.estado,
            'municipio': self.municipio,
            'colonia': self.colonia,
            'calle': self.calle,
            'costo_total': self.costo_total,
            'empleados': self.empleados
        }