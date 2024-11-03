import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel

class SecondWindow(QMainWindow):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle('Segunda Ventana')
        self.setGeometry(100, 100, 300, 200)

        # Mostrar el texto recibido
        label = QLabel(text, self)
        label.setGeometry(50, 50, 200, 50)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana Principal')
        self.setGeometry(100, 100, 300, 200)

        # Crear el widget QLineEdit para ingresar texto
        self.input = QLineEdit(self)
        self.input.setPlaceholderText('Ingresa un texto')
        self.input.setGeometry(50, 50, 200, 30)

        # Botón para enviar el texto
        self.button = QPushButton('Enviar a otra ventana', self)
        self.button.setGeometry(50, 100, 200, 30)
        self.button.clicked.connect(self.open_second_window)

    def open_second_window(self):
        # Capturar el texto ingresado en QLineEdit
        text = self.input.text()
        
        # Abrir la segunda ventana con el texto
        self.second_window = SecondWindow(text)
        self.second_window.show()

# Código para ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
