from tarifaproveedor import TarifaProveedor

class Claro(TarifaProveedor):
    
    def __init__(self, totalSMS, totalMinutos, totalGigas):
        super().__init__(totalSMS, totalMinutos, totalGigas)

    def getNombre():
        return "CLARO"
    
    def calcular (totalSMS, totalMinutos, totalGigas):
        resultado = totalSMS + totalMinutos + totalGigas
        resultado = resultado * 1.2
        return resultado