from abc import ABC
class Interfaz_Component (ABC):
    
    def __init__(self, nombre): #no deberia tener un init si es una interfaz
        self._nombre = nombre
    
    def es_carpeta ():
        pass
    
    def imprimir_contenido(self):
        pass