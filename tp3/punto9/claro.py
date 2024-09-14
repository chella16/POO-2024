from tarifaproveedor import TarifaProveedor

class Claro(TarifaProveedor):
    
    def __init__(self, totalSMS, totalMinutos, totalGigas):
        super().__init__(totalSMS, totalMinutos, totalGigas)
    
    def getNombre(self):
        return "CLARO"
    
    def calcular(self):
        resultado = super().calcular()
        resultado = resultado * 1.2
        return resultado
    
    def __str__(self):
        nombre = self.getNombre()
        return (f"En la compañia {nombre}; {super().__str__()}")
