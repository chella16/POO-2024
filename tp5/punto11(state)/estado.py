from abc import ABC
from persona import Persona
class Estado(ABC):
    
    def atender_personas (self, persona):
        pass

class Estado_Abierta (Estado):
    
    def atender_personas(self, persona):
        print(f" ATENDIENDO A  : {persona.get_nombre()} ; EDAD: {persona.get_edad()}")

class Estado_Suspendida (Estado):
    
    def atender_personas(self, persona):
        edad = persona.get_edad()
        if edad >= 60:
            print (f"ATENDIENDO A viejo: {persona.get_nombre()} ; EDAD: {edad}")
        else:
            print(f"CAJA SUSPENDIDA SOLO ATIENDE A VIEJITOS")

class Estado_Cerrado(Estado):
    
    def atender_personas(self, persona):
        print ("CAJA CERRADA NO ATIENDE A NADIE")