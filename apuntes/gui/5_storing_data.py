import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_checked = True
        self.setWindowTitle("Mi Aplicación")
        button = QPushButton("Apreta")
        button.setCheckable(True)
        button.clicked.connect(self.toggle)
        button.setChecked(self.is_checked)
        self.setCentralWidget(button)

    def toggle(self, checked):
        self.is_checked = checked
        print(self.is_checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

#que pasa si el signal no provee el estado actual? 
#ver 6 