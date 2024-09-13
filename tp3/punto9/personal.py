from tarifaproveedor import TarifaProveedor

class Personal (TarifaProveedor):
    
    def __init__(self, totalSMS, totalMinutos, totalGigas):
        super().__init__(totalSMS, totalMinutos, totalGigas)
        