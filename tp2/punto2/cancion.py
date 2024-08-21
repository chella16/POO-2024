

class Cancion:
    
    def __init__(self):
        self.__nombre = ''
        self.__autor = ''
        self.__duracion = 0.0
    
    def set_nombre (self, nombre):
        self.__nombre = nombre
    
    def get_nombre (self):
        return self.__nombre
    
    def set_autor (self, autor):
        self.__autor = autor
    
    def get_autor (self):
        return self.__autor
    
    def set_duracion (self, duracion):
        self.__duracion = duracion
    
    def get_duracion (self):
        return self.__duracion
    