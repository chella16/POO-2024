"""b. Un cuadro de diálogo que sea capaz de obtener un texto ingresado por el
usuario y que luego lo muestre en otro cuadro de diálogo."""
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class Ventana_texto (QWidget):
    
    def __init__(self, texto):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel(f" Tu texto es: {texto}")
        layout.addWidget(self.label)
        self.setLayout(layout)
    
class Ventana_principal (QMainWindow):
    
    def __init__(self):
        super(Ventana_principal, self).__init__()
        self.setWindowTitle("punto 1b")
        
        """widget = QLineEdit()
        widget.setMaxLength(20)
        widget.setPlaceholderText("INGRESE UN TEXTO DE HASTA 20 CARACTERES")"""
        self.input = QLineEdit(self)
        self.input.setMaxLength(20)
        self.input.setPlaceholderText('Ingresa un texto de hasta 20 caracteres')
        self.input.setGeometry(50,50,200,30)
        
        self.input.returnPressed.connect(self.mostrar_ventana)
        """ no entiendo porque si funciona con el self.input pero despues no, manejando el widjet no funciona del todo
        al momento de captar el texto asiq lo dejo asi, pero no puedo centrarlo bien poniendo que sea self.input"""
        ##widget.returnPressed.connect(self.mostrar_ventana)
        
        ##self.setCentralWidget(widget)
    
    def mostrar_ventana(self):
        texto = self.input.text()
        self.otra_v = Ventana_texto(texto)
        if self.otra_v.isVisible():
            self.otra_v.hide()
        else:
            self.otra_v.show()
    

aplicacion = QApplication(sys.argv)
ventana = Ventana_principal()
ventana.show()
aplicacion.exec()