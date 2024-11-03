# Si el widget no proporciona una señal que envíe el estado actual,
# tenes que recuperar el estado del widget directamente del controlador
# por ejemplo, aca se recupera el estado del boton, si esta presionado o no

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_checked = True
        self.setWindowTitle("Mi Aplicación")
        self.button = QPushButton("Apreta")
        self.button.setCheckable(True)
        self.button.released.connect(self.toggle)
        self.button.setChecked(self.is_checked)
        self.setCentralWidget(self.button)

    def toggle(self):
        self.is_checked = self.button.isChecked()
        print(self.is_checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
