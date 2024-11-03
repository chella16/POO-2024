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
    
    def formateo_argentino (self):
        fechaformateada = self.formatear_fecha(ventana_principal.dia, ventana_principal.mes, ventana_principal.año)
        self.labelfecha = f"Fecha formateada argentina: {fechaformateada}"
        montoformateado = self.formatear_moneda(ventana_principal.monto)
        self.labelmonto = f"Monto formateado a pesos: {montoformateado}"