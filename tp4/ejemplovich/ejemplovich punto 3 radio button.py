import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QRadioButton, QVBoxLayout, QWidget, QLabel


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Ejemplo de Radio Buttons")
        self.setGeometry(100, 100, 300, 200)

        # Layout principal
        layout = QVBoxLayout()

        # Etiqueta para mostrar la opción seleccionada
        self.label = QLabel("Selecciona una opción:")
        layout.addWidget(self.label)

        # Crear radio buttons
        self.radio_button1 = QRadioButton("Opción 1")
        self.radio_button2 = QRadioButton("Opción 2")
        self.radio_button3 = QRadioButton("Opción 3")

        # Añadir radio buttons al layout
        layout.addWidget(self.radio_button1)
        layout.addWidget(self.radio_button2)
        layout.addWidget(self.radio_button3)

        # Conectar los radio buttons a una función
        self.radio_button1.toggled.connect(self.mostrar_opcion_seleccionada)
        self.radio_button2.toggled.connect(self.mostrar_opcion_seleccionada)
        self.radio_button3.toggled.connect(self.mostrar_opcion_seleccionada)

        # Crear un widget contenedor
        contenedor = QWidget()
        contenedor.setLayout(layout)

        # Establecer el widget contenedor como el central de la ventana
        self.setCentralWidget(contenedor)

    def mostrar_opcion_seleccionada(self):
        # Verificar cuál radio button está seleccionado
        if self.radio_button1.isChecked():
            self.label.setText("Has seleccionado la Opción 1")
        elif self.radio_button2.isChecked():
            self.label.setText("Has seleccionado la Opción 2")
        elif self.radio_button3.isChecked():
            self.label.setText("Has seleccionado la Opción 3")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())
