"""2. Crear una interfaz gráfica de usuario (IGU) que permita seleccionar un archivo y una
ubicación de destino. Luego, al presionar un botón este archivo debe almacenarse en la
ubicación indicada."""
import sys
import shutil # para copiar archivos
import os #para trabajar con ruta de archivos
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton,  QFileDialog, QLabel, QVBoxLayout, QWidget, QMessageBox

class Ventana_Principal(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ventana godly")
        self.setGeometry(100,100,400,300)
        layout = QVBoxLayout()
        
        self.boton1 = QPushButton("Selecciona archivo mamon")
        self.boton1.clicked.connect(self.abrir_file_dialog_archivo)
        layout.addWidget(self.boton1) # boton que linkea para guardar el archivo en la ruta de destino
        
        self.boton2 = QPushButton("Seleccionar ubicacion para guardar el archivo cacamate")
        self.boton2.clicked.connect (self.abrir_file_dialog_ubicacion)
        layout.addWidget(self.boton2) # boton para seleccionar el archivo
        
        self.boton3 = QPushButton("Guardar archivo elegido en la direccion elegida gil")
        self.boton3.clicked.connect(self.copiar_archivo_ubicacion)
        layout.addWidget(self.boton3) # boton para seleccionar la ubicacion del archivo
        
        self.label1 = QLabel("direccion del archivo: ninguno pa")
        layout.addWidget(self.label1)
        self.label2 = QLabel("direccion elegida: ninguna pa")
        layout.addWidget(self.label2)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.ruta_archivo = None
        self.ruta_direccion = None
    
    def abrir_file_dialog_archivo (self):
        archivo_dialog = QFileDialog(self)
        archivo_dialog.setWindowTitle("Selecciona un archivo paa")
        
        if archivo_dialog.exec():
            self.ruta_archivo = archivo_dialog.selectedFiles()[0]  # Obtiene la ruta del archivo seleccionado
            self.label1.setText(f'Ruta del archivo: {self.ruta_archivo}')
    
    def abrir_file_dialog_ubicacion(self):
        direccion_dialog =QFileDialog(self)
        direccion_dialog.setWindowTitle ("Selecciona una ruta de destino pa")
        direccion_dialog.setFileMode(QFileDialog.FileMode.Directory)
        
        if direccion_dialog.exec():
            self.ruta_direccion = direccion_dialog.selectedFiles()[0]
            self.label2.setText(f"Ruta de destino: {self.ruta_direccion}")
    
    
    def copiar_archivo_ubicacion (self):
        if self.ruta_archivo and self.ruta_direccion:
            try:
                nombre_archivo = os.path.basename(self.ruta_archivo)
                destino = os.path.join(self.ruta_direccion,nombre_archivo)
                
                shutil.copy(self.ruta_archivo, destino)
                
                QMessageBox.information(self, "Exitooo!!", f"archivo copiado a {destino}")
                
            except Exception as e:
                QMessageBox.critical(self, "Errorrr!!", f"error al copiar el archivo en {destino}")
        
        else:
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar un archivo y una ruta de destino.")
    
# Código para ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Ventana_Principal()
    main_window.show()
    sys.exit(app.exec())