import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Aplicación")
        button = QPushButton("Apreta")
        button.setCheckable(True)
        #clicked es un signal
        button.clicked.connect(self.accion_boton)
        # Set the central widget of the Window.
        self.setCentralWidget(button)

    #slot
    def accion_boton(self):
        print("Click!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

#un signal es una señal de que ocurrio un evento con el objeto. 
#pueden seremitidas de forma explicita por el objeto, o puede
#ser de forma implícita en respuesta a un evento de sistema, 
# como un click o un cambio de foco.add()
# un slot es la funcion que se ejecuta cuando se emite un signal.
# estas responden a las signal.  