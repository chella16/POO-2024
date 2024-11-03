from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QLayout, QWidget, QMainWindow, QPushButton, QVBoxLayout, QMessageBox, QRadioButton, QLineEdit
import sys

class Vista_Principal (QMainWindow):
    
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
        self.boton1 = QPushButton("Ingrese un monto de dinero")
        layout1.addWidget(self.boton1)

        self.boton2 = QPushButton("Ingrese una fecha")
        layout1.addWidget(self.boton2)

        #boton formato YANKEE
        self.boton3_1 = QRadioButton("Formatear a argentino")
        layout1.addWidget(self.boton3_1)

        #boton formato ARGENTINO
        self.boton3_2 = QRadioButton("Formatear a yankee")
        layout1.addWidget(self.boton3_2)

        #creacion del CONTAINER donde se pone todo
        container = QWidget()
        container.setLayout(layout1)
        self.setCentralWidget(container)

class Vista_Ingreso_Monto (QWidget):
    
    def __init__(self, controlador):
        super().__init__()
        layout = QVBoxLayout()
        self.monto = None

        self.container_monto = QLineEdit()
        self.container_monto.setMaxLength(10)
        layout.addWidget(self.container_monto)
        self.setLayout(layout)

        self.container_monto.setPlaceholderText("Ingrese el monto a formatear")
        self.container_monto.editingFinished.connect(self.checkeo_monto)
        self.container_monto.clear()

        self.controlador = controlador
    
    def checkeo_monto (self):
            self.monto = self.container_monto.text()
            monto = int(self.monto)
            try:
                if monto < 0:
                    self.container_monto.clear
                    self.container_monto.setFocus
                    raise ValueError("No se admiten montos negativos")
                QMessageBox.information(self, "OK", "Monto aceptado papa")
                self.controlador.actualizarlabelmonto(monto)
                self.monto = monto
                self.close()
            except ValueError as e:
                QMessageBox.critical(self, "ERORRR!", f"Error {e}")


class Vista_Ingreso_Fecha (QWidget):
    
    def __init__(self, controlador) -> None:
        super().__init__()

        self.container_fecha = QLineEdit()
        self.container_fecha.setMaxLength(4)

        self.paso = 1

        self.container_fecha.setPlaceholderText("Ingrese el dia")
        self.container_fecha.editingFinished.connect(self.checkeo)

        layout = QVBoxLayout()
        layout.addWidget(self.container_fecha)
        self.setLayout(layout)
        
        self.controlador = controlador


    def checkeo (self):
        texto = self.container_fecha.text()
        try:
            numero = int(texto)
            if self.paso == 1:
                if numero < 1 or numero > 31:
                    raise ValueError
                else:
                    self.container_fecha.clear()
                    self.dia = numero
                    print (self.dia)
                    self.paso = 2
                    self.container_fecha.setPlaceholderText(" Ingrese el mes")
            elif self.paso == 2:
                if numero < 1 or numero > 12:
                    raise ValueError
                else:
                    self.container_fecha.clear()
                    self.mes = numero
                    print (self.mes)
                    self.paso = 3
                    self.container_fecha.setPlaceholderText(" Ingrese el año")
            elif self.paso == 3:
                if numero < 1 or numero > 9999:
                    raise ValueError
                else:
                    self.año = numero
                    print(self.año)
                    self.container_fecha.clear()
                    self.validacion_fecha(self.dia, self.mes, self.año)
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
            self.controlador.actualizarlabelfecha(dia, mes, anio)
            QMessageBox.information (self, "OK", "SE VALIDO LA FECHA PAPAAA!")
            self.close()
        except ValueError as e:
            QMessageBox.critical (self, "ERROR!",  f"Error:{e} Ingrese otra fecha")
            self.v_ventana_principal.dia_principal = None
            self.v_ventana_principal.mes_principal = None
            self.v_ventana_principal.año_principal = None