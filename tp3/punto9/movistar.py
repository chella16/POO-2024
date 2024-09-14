from tarifaproveedor import TarifaProveedor
class Movistar(TarifaProveedor):
    
    def __init__(self, totalSMS, totalMinutos, totalGigas):
        super().__init__(totalSMS, totalMinutos, totalGigas)
    
    def getNombre(self):
        return "MOVISTAR"
    
    def calcularSMS(self):
        resultado = self._totalSMS * 1.1
        return resultado
    
    def calcularMinutosDeLlamada(self):
        resultado = super().calcularMinutosDeLlamada()
        resultado = resultado * 1.2
        return resultado
    
    def calcularConsumoGB(self):
        resultado= super().calcularConsumoGB()
        resultado = resultado * 1.3
        return resultado
    
    
    def __str__(self):
        nombre = self.getNombre()
        return (f"En la compañia {nombre}; {super().__str__()}")