"""1. Desarrolle dos ejemplos del uso de un dialog:
a. Un cuadro de diálogo que indique el siguiente mensaje “Está seguro que quiere
dar de baja al usuario”, con los botones de aceptar y cancelar."""
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

class Si_Ventana(QWidget):
    def __init__(self):
        super().__init__()
        layout1 = QVBoxLayout()
        self.label1 = QLabel("Usuario dado de baja bro")
        layout1.addWidget(self.label1)
        self.setLayout(layout1)
    
class No_Ventana(QWidget):
    def __init__(self):
        super().__init__()
        layout2 = QVBoxLayout()
        self.label2 = QLabel("El usuario no fue dado de baja bro")
        layout2.addWidget(self.label2)
        self.setLayout(layout2)

class Main_Ventana (QMainWindow):
    
    def __init__(self):
        super(Main_Ventana, self).__init__()
        self.ventana_positiva = Si_Ventana()
        self.ventana_negativa = No_Ventana()
        
        layout = QVBoxLayout()
        self.setWindowTitle("punto 1 nashe")
        label1= QLabel ("Está seguro que quiere dar de baja al usuario??")
        layout.addWidget(label1)
        
        boton1 = QPushButton ("si")
        boton1.clicked.connect (
            lambda checked : self.toogle_window (self.ventana_positiva)
        )
        layout.addWidget(boton1)
        
        boton2 = QPushButton("no")
        boton2.clicked.connect (
            lambda checked : self.toogle_window (self.ventana_negativa)
        )
        layout.addWidget(boton2)
        
        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
    
    def toogle_window(self, ventana):
        if ventana.isVisible():
            ventana.hide()
        else:
            ventana.show()
    

app= QApplication(sys.argv)
w = Main_Ventana()
w.show()
app.exec()


