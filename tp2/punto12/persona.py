
class Persona:
    
    def __init__(self, persona_genero, persona_edad, persona_puesto):
        self.__persona_genero = persona_genero
        self.__persona_edad = persona_edad
        self.__persona_puesto = persona_puesto
        
    def get_persona_genero (self):
        return self.__persona_genero
    
    def set_persona_genero (self, persona_genero):
        self.__persona_genero = persona_genero
    
    def get_persona_edad (self):
        return self.__persona_edad
    
    def set_persona_edad (self, persona_edad):
        self.__persona_edad = persona_edad
    
    def str_persona__(self):
        return f"Género : {self.__persona_genero} Edad: {self.__persona_edad} Puesto de trabajo: {self.__persona_puesto}"