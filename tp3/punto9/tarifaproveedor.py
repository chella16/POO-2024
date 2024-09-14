from abc import ABC

class TarifaProveedor(ABC):
    
    def __init__(self, totalSMS, totalMinutos, totalGigas) :
        self._totalSMS = totalSMS
        self._totalMinutos = totalMinutos
        self._totalGigas = totalGigas
    
    #@abstractmethod
    def calcularMinutosDeLlamada(self):
        resultado = 0
        resultado = self._totalMinutos * 15
        return resultado
    
    #@abstractmethod
    def calcularConsumoGB(self):
        return (self._totalGigas * 20)
    
    def calcular (self):
        resultado = self._totalSMS + self.calcularMinutosDeLlamada() + self.calcularConsumoGB()
        return resultado
    
    #@abstractmethod
    def getNombre():
        pass
    
    def __str__(self) :
        return (f" Con: {self._totalSMS} Mensajes; Con {self._totalMinutos} Minutos de llamada  y Con {self._totalGigas} Gigas consumidos tu tarifa es de {self.calcular()}")