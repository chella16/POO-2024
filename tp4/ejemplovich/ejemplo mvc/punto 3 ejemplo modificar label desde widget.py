import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

# Clase QMainWindow donde está el QLabel que queremos modificar
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 300)

        # Crear un QLabel
        self.label = QLabel("Texto original", self)
        self.label.setGeometry(100, 50, 200, 50)

        # Crear una instancia de la clase CustomWidget y pasar la referencia de self (MainWindow)
        self.widget = CustomWidget(self)
        self.setCentralWidget(self.widget)

# Clase QWidget que interactúa con el QLabel en MainWindow
class CustomWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()

        # Guardamos la referencia de la ventana principal
        self.main_window = main_window

        # Botón para cambiar el texto del QLabel
        self.button = QPushButton("Cambiar texto", self)
        self.button.clicked.connect(self.cambiar_texto)

        # Layout del widget
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    # Método para modificar el QLabel en MainWindow
    def cambiar_texto(self):
        self.main_window.label.setText("Texto modificado desde CustomWidget")

# Función principal de la aplicación
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())