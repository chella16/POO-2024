from abc import ABC
import random
class Observable(ABC):
    
    def agregar_subs (self, observer):
        pass
    
    def eliminar_subs (self,observer):
        pass
    
    def notificar (self):
        pass
    

class Sistema_meteorologico (Observable):
    
    def __init__(self):
        self._estado_clima = ""
        self._suscriptores = []
    
    def agregar_subs(self, observer):
        self._suscriptores.append(observer)
    
    def eliminar_subs(self,observer):
        self._suscriptores.remove(observer)
    
    def notificar(self):
        print (f"CAMBIO DE CLIMA a {self._estado_clima}")
        for observer in self._suscriptores:
            observer.actualizar(self)
    
    def detectar_cambio_estado(self):
        cambio = False
        while not cambio:
            print("Detectando si cambia el clima")
            cambio = bool(random.getrandbits(1))
        clima = ["lluvioso","ventoso", "soleado", "nublado", "cigüeña"]
        estado = random.choice (clima)
        self._estado_clima = estado
        print (f"CAMBIO A: {estado}")
        self.notificar()
