import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QDialog, QDialogButtonBox


# Modelo
class Modelo:
    def __init__(self):
        self.texto = ""

    def set_texto(self, nuevo_texto):
        self.texto = nuevo_texto

    def get_texto(self):
        return self.texto


# Vista de la ventana secundaria para ingresar texto
class VistaDialogo(QDialog):
    def __init__(self, controlador, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Definir el campo de texto y los botones de aceptar/cancelar
        self.input_texto = QLineEdit(self)
        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input_texto)
        layout.addWidget(botones)
        self.setLayout(layout)

        # Conectar las señales de los botones
        botones.accepted.connect(self.aceptar)
        botones.rejected.connect(self.reject)

        # Guardar el controlador para poder actualizar el modelo desde aquí
        self.controlador = controlador

    def aceptar(self):
        # Obtener el texto del QLineEdit y usar el controlador para actualizar el modelo
        nuevo_texto = self.input_texto.text()
        self.controlador.actualizar_texto(nuevo_texto)
        self.accept()


# Vista principal con QMainWindow
class VistaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Definir un QLabel para mostrar el texto
        self.label = QLabel("Texto inicial", self)

        # Definir un botón que abre la ventana secundaria
        self.boton = QPushButton("Abrir ventana para modificar texto", self)

        # Configurar la ventana principal
        self.setWindowTitle('Ejemplo QMainWindow y Dialogo')
        self.setGeometry(100, 100, 400, 200)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.boton)

        # Widget central para QMainWindow
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


# Controlador
class Controlador:
    def __init__(self, modelo, vista_principal):
        self.modelo = modelo
        self.vista_principal = vista_principal

        # Conectar el botón de la vista principal para abrir la ventana secundaria
        self.vista_principal.boton.clicked.connect(self.abrir_ventana_ingresar_texto)

    def abrir_ventana_ingresar_texto(self):
        # Crear y mostrar el diálogo para ingresar texto
        dialogo = VistaDialogo(self)
        dialogo.exec()  # Mostrar la ventana de diálogo de forma modal

    def actualizar_texto(self, nuevo_texto):
        # Actualizar el modelo con el nuevo texto
        self.modelo.set_texto(nuevo_texto)

        # Actualizar la vista principal (QLabel) con el nuevo texto del modelo
        self.vista_principal.label.setText(self.modelo.get_texto())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Instanciar el modelo, la vista principal y el controlador
    modelo = Modelo()
    vista_principal = VistaPrincipal()
    controlador = Controlador(modelo, vista_principal)

    # Mostrar la ventana principal
    vista_principal.show()

    sys.exit(app.exec())