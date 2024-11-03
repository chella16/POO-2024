import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi App")

        button = QPushButton("Click para un Dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("¡Aviso!")
        dlg.setText("Este es un dialog que sirve para mostrar un aviso.")
       # dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:
            print("OK!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

#QMessageBox.StandardButton.Ok
#QMessageBox.StandardButton.Open
#QMessageBox.StandardButton.Save
#QMessageBox.StandardButton.Cancel
#QMessageBox.StandardButton.Close
#QMessageBox.StandardButton.Discard
#QMessageBox.StandardButton.Apply
#QMessageBox.StandardButton.Reset
#QMessageBox.StandardButton.RestoreDefaults
#QMessageBox.StandardButton.Help
#QMessageBox.StandardButton.SaveAll
#QMessageBox.StandardButton.Yes
#QMessageBox.StandardButton.YesToAll
#QMessageBox.StandardButton.No
#QMessageBox.StandardButton.NoToAll
#QMessageBox.StandardButton.Abort
#QMessageBox.StandardButton.Retry
#QMessageBox.StandardButton.Ignore
#QMessageBox.StandardButton.NoButton