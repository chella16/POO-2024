from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QLayout, QWidget, QMainWindow, QPushButton, QVBoxLayout, QMessageBox, QRadioButton, QLineEdit
from interfaz_metodos_formatear import Interfaz_metodos_formatear
import sys

#-----------------------------------------------------------------------------------------------------------
class formato_estadounidense (Interfaz_metodos_formatear):
    
    def __init__(self):
        super().__init__()
    
    def formatear_moneda(cantidad):
        dolares = cantidad / 1215
        return dolares
    
    def formatear_fecha(dia, mes, año):
        fecha = f"{mes} / {dia} / {año}"
        return fecha
    
    def formateo_estadounidense (self):
        fechaformateada = self.formatear_fecha(ventana_principal.dia_principal, ventana_principal.mes_principal, ventana_principal.año_principal)
        self.labelfecha = f"Fecha formateada estadounidense: {fechaformateada}"
        montoformateado = self.formatear_moneda(ventana_principal.monto)
        self.labelmonto = f"Monto formateado a dolares: {montoformateado}"
#-----------------------------------------------------------------------------------------------------------
class formato_argentino (Interfaz_metodos_formatear):
    
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
#-----------------------------------------------------------------------------------------------------------
class ventana_ingreso_fecha (QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        self.v_ventana_principal = ventana_principal
        
        self.container_fecha = QLineEdit()
        self.container_fecha.setMaxLength(4)
        
        self.paso = 1
        self.container_fecha.setPlaceholderText("Ingrese el dia")
        self.container_fecha.editingFinished.connect(self.checkeo)
        
        layout.addWidget(self.container_fecha)
        self.setLayout(layout)
    
    def checkeo (self):
        texto = self.container_fecha.text()
        try:
            numero = int(texto)
            if self.paso == 1:
                if numero < 1 or numero > 31:
                    raise ValueError
                else:
                    self.container_fecha.clear()
                    self.v_ventana_principal.dia_principal = numero
                    print (self.v_ventana_principal.dia_principal)
                    self.paso = 2
                    self.container_fecha.setPlaceholderText(" Ingrese el mes")
            elif self.paso == 2:
                if numero < 1 or numero > 12:
                    raise ValueError
                else:
                    self.container_fecha.clear()
                    self.v_ventana_principal.mes_principal = numero
                    print (self.v_ventana_principal.mes_principal)
                    self.paso = 3
                    self.container_fecha.setPlaceholderText(" Ingrese el año")
            elif self.paso == 3:
                if numero < 1 or numero > 9999:
                    raise ValueError
                else:
                    self.v_ventana_principal.año_principal = numero
                    print(self.v_ventana_principal.año_principal)
                    self.container_fecha.clear()
                    dia = self.v_ventana_principal.dia_principal
                    mes = self.v_ventana_principal.mes_principal
                    año = self.v_ventana_principal.año_principal
                    self.validacion_fecha(dia, mes, año)
        except ValueError:
                QMessageBox.critical(self, " ERROOR ", "Ingrese un parametro valido para el tipo")
                self.container_fecha.clear()
                self.container_fecha.setFocus()

    def validacion_fecha (self, dia, mes, anio):
        anio= int(anio)
        dia = int(dia)
        mes = int(mes)
        try:
            biciesto = anio % 4
            if biciesto == 0 and mes == 2 and dia > 29:
                raise ValueError("En un año biciesto febrero no tiene mas de 29 dias")
            if biciesto != 0 and mes == 2 and dia >= 29:
                raise ValueError("En un año normal febrero no tiene mas de 28 dias")
            if (mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia == 31:
                raise ValueError("Este mes no puede tener 31 dias")
            self.v_ventana_principal.modificarlabel1(dia, mes, anio)
            QMessageBox.information (self, "OK", "SE VALIDO LA FECHA PAPAAA!")
        except ValueError as e:
            QMessageBox.critical (self, "ERROR!",  f"Error:{e} Ingrese otra fecha")
            self.v_ventana_principal.dia_principal = None
            self.v_ventana_principal.mes_principal = None
            self.v_ventana_principal.año_principal = None
#-----------------------------------------------------------------------------------------------------------
class ventana_ingreso_monto (QWidget):
    
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.container_monto = QLineEdit()
        self.container_monto.setMaxLength(10)
        layout.addWidget(self.container_monto)
        self.setLayout(layout)
        
        #creacion de objeto tipo MAIN WINDOW
        self.v_ventana_principal = ventana_principal
        
        self.monto = 0 #variable para setear el qlabel
        
        self.container_monto.setPlaceholderText("Ingrese el monto a formatear")
        self.container_monto.editingFinished.connect(self.checkeo_monto)
        self.container_monto.clear()
    
    def checkeo_monto (self):
        monto = self.container_monto.text()
        monto = int(self.monto)
        try:
            if monto < 0:
                self.container_fecha.clear
                self.container_fecha.setFocus
                raise ValueError("No se admiten montos negativos")
            QMessageBox.information(self, "OK", "Monto aceptado papa")
            self.cambiar_label(monto)
            #self.v_ventana_principal.modificarlabelmonto(monto)
            self.close()
            #self.v_ventana_principal.labelmonto.setText(f"Monto ingresado: {self.monto}")
            #self.v_ventana_principal.modificarlabelmonto(f"Monto ingresado: {monto}")
        except ValueError as e:
            QMessageBox.critical(self, "ERORRR!", f"Error {e}")
        
    
    def cambiar_label (self,monto):
        print('entra')
        self.v_ventana_principal.get_labelmonto().setText(f"Monto ingresado: {monto}")
#-----------------------------------------------------------------------------------------------------------
class ventana_principal (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formateo de moneda y fecha")
        self.setGeometry(100,100,400,300)
        layout1 = QVBoxLayout()
        
        #labels:
        self.labelfecha = QLabel("Fecha ingresada: Ninguna", self)
        layout1.addWidget(self.labelfecha)
        self.labelmonto = QLabel("Monto ingresado: None", self)
        layout1.addWidget(self.labelmonto)
        
        #interfaz MONTO DINERO
        self.montoprincipal = 1 # variable principal para llamar al formateo de la clase
        self.ventana_monto = ventana_ingreso_monto()
        self.boton1 = QPushButton("Ingrese un monto de dinero")
        self.boton1.clicked.connect(self.toggle_ventana_monto)
        layout1.addWidget(self.boton1)
        
        #interfaz FECHA
        self.dia_principal = None #variable principal para llamar en el formateo de fecha
        self.mes_principal = None #variable principal para llamar en el formateo de fecha
        self.año_principal = None #variable principal para llamar en el formateo de fecha
        self.ventana_fecha = ventana_ingreso_fecha()
        self.boton2 = QPushButton("Ingrese una fecha")
        self.boton2.clicked.connect(self.toggle_ventana_fecha)
        layout1.addWidget(self.boton2)
        
        #boton formato YANKEE
        self.boton3_1 = QRadioButton("Formatear a estadounidense")
        layout1.addWidget(self.boton3_1)
        self.boton3_1.toggled.connect(formato_estadounidense.formateo_estadounidense)
        
        #boton formato ARGENTINO
        self.boton3_2 = QRadioButton("Formatear a argentino papa")
        layout1.addWidget(self.boton3_2)
        self.boton3_2.toggled.connect(formato_argentino.formateo_argentino)
        
        #creacion del CONTAINER donde se pone todo
        container = QWidget()
        container.setLayout(layout1)
        self.setCentralWidget(container)
    
    def set_dia (self,dia):
        self.dia_principal = dia
    
    def get_dia (self):
        return self.dia_principal
    
    def set_mes (self,mes):
        self.mes_principal = mes
    
    def get_mes (self):
        return self.mes_principal
    
    def set_año (self,año):
        self.año_principal = año
    
    def get_año (self):
        return self.año_principal
    
    def modificarlabelmonto (self, montonuevo):
        self.labelmonto.setText(f"Monto ingresado: {montonuevo}")
    
    def get_labelmonto (self):
        return self.labelmonto
    
    def modificarlabel1 (self, dia, mes, anio):
        self.labelfecha.setText(f"Fecha ingresada: dia:{dia}, mes: {mes}, año. {anio} ")
    
    def toggle_ventana_fecha(self, checked):
        if self.ventana_fecha.isVisible():
            self.ventana_fecha.hide()
        else:
            self.ventana_fecha.show()
    
    def toggle_ventana_monto(self, checked):
        if self.ventana_monto.isVisible():
            self.ventana_monto.hide()
        else:
            self.ventana_monto.show()
#-----------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ventana_principal()
    ventana.show()
    sys.exit(app.exec())