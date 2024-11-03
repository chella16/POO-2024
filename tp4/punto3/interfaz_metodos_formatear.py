from abc import ABC, abstractmethod
class Interfaz_metodos_formatear(ABC):
    
    def __init__ (self):
        pass
    
    @abstractmethod
    def formatear_moneda (cantidad):
        pass
    
    @abstractmethod
    def formatear_fecha (dia, mes, año):
        pass
    