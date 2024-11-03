from abc import ABC
class Observer (ABC):
    
    def actualizar (self, observable):
        pass
    

class Reportero (Observer):
    
    def actualizar (self, observable):
        print ( " " * (4) + "El reportero indica que el sistema meteorologico dice que hay cambio de clima ")