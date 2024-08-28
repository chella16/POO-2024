
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
    
    
    #def permiso_trabajar_manejar (self):
        #if self.__persona_edad < 16:
            #self.__persona_permiso_trabajar = False
            #self.__persona_licencia_conducir = False
        #if self.__persona_edad < 17:
            #self.__persona_permiso_trabajar = True
            #self.__persona_licencia_conducir = False
        #else:
            #self.__persona_permiso_trabajar = True
            #self.__persona_licencia_conducir = True
        #return 
    #(?? por que no me configura bien las cosas??? :(  )
    
    def __str_persona__(self):
        rta_trabaja = "no"
        rta_estudia = "no"
        rta_permiso_trabajo = "no"
        rta_licencia_conducir = "no"
        if self.__persona_trabaja:
            rta_trabaja= "si"
        if self.__persona_estudia:
            rta_estudia= "si"
        if self.__persona_edad >= 16:
            rta_permiso_trabajo = "si"
        if self.__persona_edad >= 17:
            rta_licencia_conducir = "si"
        
        return f"Género : {self.__persona_genero} Edad: {self.__persona_edad} Estudia: {rta_estudia} Trabaja: {rta_trabaja} Puede trabajar? {rta_permiso_trabajo}  Puede sacar la licencia de conducir? {rta_licencia_conducir}"