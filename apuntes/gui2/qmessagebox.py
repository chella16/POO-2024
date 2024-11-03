import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton,QMessageBox
from custom_dialog import CustomDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi App")

        button = QPushButton("Click para un Dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        button = QMessageBox.question(self, "Titulo", "Cuerpo del mensaje")

        if button == QMessageBox.StandardButton.Yes:
            print("Si!")
        else:
            print("No!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()