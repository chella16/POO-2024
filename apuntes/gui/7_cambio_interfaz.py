import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Aplicación")
        self.button = QPushButton("Apreta")
        self.button.clicked.connect(self.click)

        self.setCentralWidget(self.button)

    def click(self):
        self.button.setText("click!.")
        self.button.setEnabled(False) #deshabilita boton

        # cambia titulo de ventana.
        self.setWindowTitle("Hiciste Click")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()