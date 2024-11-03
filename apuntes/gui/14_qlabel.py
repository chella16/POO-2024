import sys
from PyQt6.QtWidgets import  QMainWindow, QApplication, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Mi App")
        lbl1 = QLabel("Hola!")
        font = lbl1.font()
        font.setPointSize(30)
        lbl1.setFont(font)
        lbl1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.setCentralWidget(lbl1)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()