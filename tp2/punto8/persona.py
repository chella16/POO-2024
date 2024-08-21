
class Persona:
    
    def __init__(self, persona_genero, persona_edad, trabaja, estudia):
        self.__persona_genero = persona_genero
        self.__persona_edad = persona_edad
        self.__persona_trabaja = trabaja
        self.__persona_estudia = estudia
        
    def get_persona_genero (self):
        return self.__persona_genero
    
    def set_persona_genero (self, persona_genero):
        self.__persona_genero = persona_genero
    
    def get_persona_edad (self):
        return self.__persona_edad
    
    def set_persona_edad (self, persona_edad):
        self.__persona_edad = persona_edad
    
    def get_persona_trabaja (self):
        return self.__persona_trabaja
    
    def set_persona_trabaja (self, persona_trabaja):
        self.__persona_trabaja = persona_trabaja
    
    def get_persona_estudia (self):
        return self.__persona_estudia
    
    def set_persona_estudia (self, persona_estudia):
        self.__persona_estudia = persona_estudia
    
    def __str_persona__(self):
        rta_trabaja = "no"
        rta_estudia = "no"
        if self.__persona_trabaja:
            rta_trabaja= "si"
        if self.__persona_estudia:
            rta_estudia= "si"
        return f"Género : {self.__persona_genero} Edad: {self.__persona_edad} Estudia: {rta_estudia} Trabaja: {rta_trabaja}"