from abc import ABC
class Observable (ABC):
    
    def agregar(self, observer):
        pass
    
    def eliminar(self, observer):
        pass
    
    def notificar (self):
        pass

import random
class Boya_de_mar (Observable):
    
    def __init__(self):
        self.__nombre = "La boya de mar"
        self.__salinidad = ""
        self.__temperatura = ""
        self.__lista_subs = []
    
    def get_nombre (self):
        return self.__nombre
    
    def agregar(self, observer):
        self.__lista_subs.append(observer)
    
    def eliminar(self, observer):
        self.__lista_subs.remove(observer)
    
    def notificar(self):
        print (f"SE DETECTO CAMBIO EN EL MAR; temperatura en el mar: {self.__temperatura}; salinidad: {self.__salinidad}")
        for observer in self.__lista_subs:
            observer.actualizar()
    
    def detectar_cambio (self):
        cambio = False
        while not cambio:
            print("Detectando si cambia la salinidad o temperatura en el mar")
            cambio = bool(random.getrandbits(1))
        self.__temperatura = random.uniform(1, 23)
        self.__salinidad = random.random
        self.notificar()

class Estacion_Meteorologica (Observable):
    
    def __init__(self):
        self.__nombre = "La estacion meteorologica"
        self.__presion_atmosferica = ""
        self.__temperatura = ""
        self.__velocidad_viento = ""
        self.__lista_subs = []
    
    def get_nombre (self):
        return self.__nombre
    
    def agregar(self, observer):
        self.__lista_subs.append(observer)
    
    def eliminar(self, observer):
        self.__lista_subs.remove(observer)
    
    def notificar(self):
        print (f"SE DETECTO CAMBIO EN TIERRA; temperatura: {self.__temperatura}; presion atmosferica: {self.__presion_atmosferica}")
        for observer in self.__lista_subs:
            observer.actualizar()
    
    def detectar_cambio (self):
        cambio = False
        while not cambio:
            print("Detectando si cambia la salinidad o temperatura en el mar")
            cambio = bool(random.getrandbits(1))
        self.__temperatura = random.uniform(1, 23)
        self.__salinidad = random.random
        self.notificar()