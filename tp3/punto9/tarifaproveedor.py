from abc import ABC

class TarifaProveedor(ABC):
    
    def __init__(self, totalSMS, totalMinutos, totalGigas) :
        self._nombre_proveedor = ""
    
    def calcularSMS(totalSMS):
        return totalSMS
    
    #@abstractmethod
    def calcularMinutosDeLlamada(totalMinutos):
        pass
    
    #@abstractmethod
    def calcularConsumoGB(totalGigas):
        pass
    
    def calcular (totalSMS, totalMinutos, totalGigas):
        resultado = totalSMS + totalMinutos + totalGigas
        return resultado
    
    #@abstractmethod
    def getNombre():
        pass