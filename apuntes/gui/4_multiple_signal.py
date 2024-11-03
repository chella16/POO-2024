import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Aplicación")
        button = QPushButton("Apreta")
        button.setCheckable(True)
        button.clicked.connect(self.accion_boton)
        button.clicked.connect(self.was_toggle)
        self.setCentralWidget(button)

    def accion_boton(self):
        print("Click!")

    def was_toggle(self, checked):
        print("Check?", checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()