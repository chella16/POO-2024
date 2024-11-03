
class Persona():
    
    def __init__(self, nombre, edad):
        self.__nombre_persona = nombre
        self.__edad_persona = edad
    
    def get_nombre (self):
        return self.__nombre_persona
    
    def get_edad (self):
        return self.__edad_persona
    