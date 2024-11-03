from vista import Vista_Ingreso_Fecha, Vista_Ingreso_Monto
from formateo import Formato_Argentino, Formato_Yankee

class Controlador:
    def __init__(self, Modelo, vista_principal):
        self.modelo = Modelo
        self.vista_principal = vista_principal
        
        self.vista_principal.boton1.clicked.connect (self.abrir_ventana_monto)
        self.vista_principal.boton2.clicked.connect (self.abrir_ventana_fecha)
        self.vista_principal.boton3_1.toggled.connect(self.formatear_argentino)
        self.vista_principal.boton3_2.toggled.connect(self.formatear_yankee)
    
    def abrir_ventana_monto(self):
        self.ingreso_monto = Vista_Ingreso_Monto(self)
        if self.ingreso_monto.isVisible():
            self.ingreso_monto.hide()
        else:
            self.ingreso_monto.show()
    
    def actualizarlabelmonto (self, montonuevo):
        self.modelo.set_monto(montonuevo)
        self.vista_principal.labelmonto.setText(self.modelo.get_monto())
    
    def abrir_ventana_fecha (self):
        self.ingreso_fecha = Vista_Ingreso_Fecha(self)
        if self.ingreso_fecha.isVisible():
            self.ingreso_fecha.hide()
        else:
            self.ingreso_fecha.show()
    
    def actualizarlabelfecha (self, dia, mes, año):
        self.modelo.set_fecha(dia, mes, año)
        self.vista_principal.labelfecha.setText(self.modelo.get_fecha())
    
    def formatear_argentino (self):
        monto = self.modelo.get_montoneto()
        monto = Formato_Argentino.formatear_moneda(monto)
        self.modelo.set_montoargentino(monto)
        self.vista_principal.labelmonto.setText(self.modelo.get_monto())
    
    def formatear_yankee (self):
        monto = self.modelo.get_montoneto()
        monto = Formato_Yankee.formatear_moneda(monto)
        self.modelo.set_montoyankee(monto)
        self.vista_principal.labelmonto.setText(self.modelo.get_monto())