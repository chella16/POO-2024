import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QLabel, QMessageBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Validación de QLineEdit")
        self.setGeometry(100, 100, 400, 200)

        # Layout principal
        layout = QVBoxLayout()

        # Etiqueta de instrucciones
        self.label = QLabel("Ingresa un texto que solo contenga letras (A-Z):")
        layout.addWidget(self.label)

        # Crear QLineEdit para la entrada de texto
        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        # Conectar la señal de edición finalizada
        self.line_edit.editingFinished.connect(self.validar_texto)

        # Crear un widget contenedor
        contenedor = QWidget()
        contenedor.setLayout(layout)

        # Establecer el widget contenedor como el central de la ventana
        self.setCentralWidget(contenedor)

    def validar_texto(self):
        texto = self.line_edit.text()

        # Condición de validación: solo letras (A-Z)
        if not texto.isalpha():
            # Mostrar mensaje de advertencia
            QMessageBox.warning(self, "Error de validación", "El texto ingresado no es válido. Solo se permiten letras (A-Z).")

            # Limpiar el texto y devolver el foco al QLineEdit
            self.line_edit.clear()
            self.line_edit.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())
