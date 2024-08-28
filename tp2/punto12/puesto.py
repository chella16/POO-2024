
class Puesto:
    
    def __init__(self, nombre_puesto):
        self.__nombre_puesto = nombre_puesto
    
    def get_nombre_puesto (self):
        return self.__nombre_puesto
    
    def set_nombre_puesto (self, nombre_puesto):
        self.__nombre_puesto = nombre_puesto
        
    def __str__(self) -> str:
        return self.__nombre_puesto