import sys
from PyQt6.QtWidgets import  QMainWindow, QApplication, QLineEdit
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Mi App")
        
        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Ingrese un texto")

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)


    def return_pressed(self):
        print("Apreto enter")
        self.centralWidget().setText("ENTER!")

    def selection_changed(self):
        print("Se selecciono")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Texto modificado...")
        print(s)

    def text_edited(self, s):
        print("Texto editado...")
        print(s) 

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()