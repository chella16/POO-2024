from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Otra ventana")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        #self.w = None  
        self.button = QPushButton("Click para una nueva ventana")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        w = AnotherWindow()
        w.show()
        
        #self.w= AnotherWindow()
        #self.w.show()

        #if self.w is None:
        #    self.w = AnotherWindow()
        #self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()