
class Alumno:
    __nombre = " "
    __apellido = " "
    __dni = 0
    def __init__ (self):
        pass
        
    @classmethod
    def iniciar (cls):
        alumno = cls.__new__(cls)
        alumno.__nombre = " "
        alumno.__apellido = " "
        alumno.__dni = 0
        return alumno
    
    def set_nombre (self, nombre):
        self.__nombre = nombre
    
    def set_apellido (self, apellido):
        self.__apellido = apellido
    
    def set_dni (self, dni):
        self.__dni = dni
    
    def get_dni (self):
        return self.__dni
    
    @classmethod
    def iniciar_con_nom_ape(cls, nombre, apellido):
        alumno =cls.__new__(cls)
        alumno.__nombre = nombre
        alumno.__apellido = apellido
        return alumno
    
    def get_nombre_y_apellido (self):
        return f"{self.__nombre} {self.__apellido}"
    
    #cacamate
        