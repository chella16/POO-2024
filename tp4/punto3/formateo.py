from interfaz_metodos_formatear import Interfaz_metodos_formatear

class Formato_Argentino(Interfaz_metodos_formatear):
    
    def __init__(self):
        super().__init__()
    
    def formatear_moneda(cantidad):
        pesos = cantidad * 1215
        return pesos
    
    def formatear_fecha(dia, mes, año):
        fecha = f"{dia} / {mes} / {año}"
        return fecha

class Formato_Yankee (Interfaz_metodos_formatear):
    
    def __init__(self):
        super().__init__()
    
    def formatear_moneda(cantidad):
        dolares = cantidad / 1215
        return dolares
    
    def formatear_fecha(dia, mes, año):
        fecha = f"{mes} / {dia} / {año}"
        return fecha