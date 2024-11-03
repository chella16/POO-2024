from abc import ABC
class Observer(ABC):
    
    def actualizar(self):
        pass

class Centro_Control(Observer):
    
    def actualizar(self, observable):
        print (" " * 4 + f"Centro de control: Hubo cambios en {observable.get_nombre()}")