
class Persona:
    
    def __init__(self, nombre, apellido, fecha):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha
        
    def get_nombre (self):
        return self.__nombre
    
    def set_nombre (self, nombre):
        self.__nombre = nombre
    
    def get_apellido (self):
        return self.__apellido
    
    def set_apellido (self, apellido):
        self.__apellido = apellido
    
    def get_fecha_nacimiento (self):
        return self.__fecha_nacimiento
    
    def set_fecha_nacimiento (self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento
    
    def __str__(self):
        return f"nombre: {self.__nombre}, apellido: {self.__apellido}, fecha nacimiento: {self.__fecha_nacimiento}"
    