from interfaz import Interfaz_Component
class Archivo (Interfaz_Component):
    
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def es_carpeta():
        return False
    
    def imprimir_contenido(self, i):
        print(" " * (4*i) + self._nombre )