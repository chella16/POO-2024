from estado import Estado_Cerrado
class Banco():
    
    def __init__(self, nombre):
        self.__estado_caja = Estado_Cerrado()
        self.__nombre_caja = nombre
    
    def set_estado_banco(self, estado):
        self.__estado_caja = estado
    
    def get_estado_banco (self):
        return self.__estado_caja
    
    def atender_personas(self, persona):
        print (f"EL banco {self.__nombre_caja}")
        self.__estado_caja.atender_personas(persona)
    

