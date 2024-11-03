import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

#cuando se dice Event, es un tipo de signal que se emite 
# en respuesta a una acción del usuario o del sistema. 
#signal es un concepto mas general y evento mas especifico. 
#ejemplo de signal que no es event:
    #changed (cuando un valor cambia)
    #finished (cuando una operación finaliza)
    #error (cuando ocurre un error)
#ejemplo de evento:
    #clicked cuando el usuario hace click en el objeto
    #key_pressed cuando el usuario presiona una tecla
    #mouse_moved cuando el usuario mueve el cursor
    