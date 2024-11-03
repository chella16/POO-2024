from PyQt6.QtWidgets import QApplication
from modelo import Modelo
from controlador import Controlador
from vista import Vista_Principal, Vista_Ingreso_Fecha, Vista_Ingreso_Monto
import sys

if __name__ =='__main__':
    app = QApplication(sys.argv)
    
    modelomain = Modelo()
    vista_principal_main = Vista_Principal()
    controladormain = Controlador (modelomain, vista_principal_main)
    
    vista_principal_main.show()
    
    sys.exit(app.exec())
    