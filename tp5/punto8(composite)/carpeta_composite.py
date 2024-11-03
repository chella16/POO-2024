from interfaz import Interfaz_Component
class Carpeta (Interfaz_Component):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        self._lista_componentes = []
    
    def es_carpeta():
        return True
    
    def agregar_componente (self, componente):
        self._lista_componentes.append(componente)
    
    def eliminar_componente (self, componente):
        self._lista_componentes.pop()
    
    def imprimir_contenido (self, i=0):
        print (" " * (4*i) + self._nombre)
        i = i+1
        if self.es_carpeta:
            for componente in self._lista_componentes:
                componente.imprimir_contenido(i)
    
    