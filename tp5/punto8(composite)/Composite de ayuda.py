from abc import ABC, abstractmethod

class Component(ABC):
    
    @abstractmethod
    def esCarpeta(self):
        pass
    
    @abstractmethod
    def imprimirNombre(self):
        pass


class Carpeta(Component):#seria el Composite
    def __init__(self,nombre) -> None:
        self._nombre = nombre
        self._children:list[Component] = []
        
    def add(self,component: Component):
        self._children.append(component)
    
    def remove(self,component:Component):
        self._children.remove(component)
    
    def esCarpeta(self):
        return True

    def imprimirNombre(self, i = 0):
        
        print( " "*i + f"{self._nombre}")
        i +=2
        
        for elem in self._children:
            elem.imprimirNombre(i)
    
    
class Archivo(Component): #seria el Leaf
    def __init__(self,nombre) -> None:
        self._nombre = nombre
    
    def esCarpeta(self):
        return False
    
    def imprimirNombre(self,i):
        print(" "*i + f"*{self._nombre}")
    

oCarpeta1 = Carpeta("Carpeta 1")
oCarpeta2 = Carpeta("Carpeta 2")
oCarpeta3 = Carpeta("Carpeta 3")
oArchivo1 = Archivo("Archivo 1")
oArchivo2 = Archivo("Archivo 2")
oArchivo3 = Archivo("Archivo 3")
oArchivo4 = Archivo("Archivo 4")

oCarpeta1.add(oCarpeta2)
oCarpeta2.add(oArchivo1)
oCarpeta2.add(oArchivo2)
oCarpeta1.add(oArchivo3)
oCarpeta3.add(oArchivo4)

oCarpeta1.imprimirNombre()
oCarpeta3.imprimirNombre()