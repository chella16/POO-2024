from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #inicializo label, input
        self.setWindowTitle("Mi App")
        self.label = QLabel()
        self.input = QLineEdit()
        #conecto input con label
        #textChanged es un signal
        #setText es un slot
        self.input.textChanged.connect(self.label.setText)
       #creo un layout y agrego los elementos.
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        #creo un contenedor, agrego el layout y lo agrego a la ventana
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

#buscar mas signal y slots en https://doc.qt.io/qt-6/ 