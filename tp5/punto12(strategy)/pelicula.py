
class Pelicula ():
    
    def __init__(self, nombre, mayores_de):
        self.__nombre = nombre
        self.__clasificacion = mayores_de
    
    def get_nombre (self):
        return self.__nombre
    
    def get_clasificacion (self):
        return self.__clasificacion
