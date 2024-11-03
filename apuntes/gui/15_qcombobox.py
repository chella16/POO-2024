import sys
from PyQt6.QtWidgets import  QMainWindow, QApplication, QComboBox
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Mi App")
        widget = QComboBox()
        widget.addItems(["Uno", "Dos", "Tres"])

        # Envia la posición actual del item seleccionado.
        widget.currentIndexChanged.connect( self.index_changed )

        # Otro Signal para poder capturar el evento
        widget.currentTextChanged.connect( self.text_changed )

        self.setCentralWidget(widget)


    def index_changed(self, i): # i es un int
        print(i)

    def text_changed(self, s): # s es un str
        print(s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()