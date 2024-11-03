
class Modelo:
    
    def __init__(self):
        self.fecha = ""
        self.monto = ""
        self.dia = ""
        self.mes = ""
        self.año = ""
        self.montoneto =""
    
    def set_fecha (self, dia, mes, año):
        self.fecha = f"Fecha ingresada: dia --> {dia}, mes --> {mes}, año --> {año} "
    
    def get_fecha (self):
        return self.fecha
    
    def set_monto (self, montonuevo):
        self.monto = f"Monto ingresado: {montonuevo} en dolares o pesos XD"
        self.montoneto = montonuevo
    
    def set_montoargentino (self, montonuevo):
        self.monto = f"""El monto ingresado fue: {self.montoneto} en dolare$
        El monto formateado a Argentino: {montonuevo} pesos"""
        self.montoneto = montonuevo
    
    def set_montoyankee (self, montonuevo):
        self.monto = f"""El monto ingresado fue: {self.montoneto} en pesos$
        El monto formateado a Yankee: {montonuevo} dolares"""
        self.montoneto = montonuevo
    
    def get_monto (self):
        return self.monto
    
    def get_montoneto (self):
        return self.montoneto
    
    def get_dia (self):
        return self.dia
    
    def get_mes (self):
        return self.mes
    
    def get_año (self):
        return self.año