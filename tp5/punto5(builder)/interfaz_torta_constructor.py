from abc import ABC, abstractmethod
class Interfaz_Torta (ABC):
    
    def __init__(self):
        pass
    
    @abstractmethod
    def resetear (self):
        pass
    
    @abstractmethod
    def crear_masa (self, masa):
        pass
    
    @abstractmethod
    def crear_relleno (self, relleno):
        pass