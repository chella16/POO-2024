from interfaz_torta_constructor import Interfaz_Torta
from torta import Torta
class Constructor_Torta (Interfaz_Torta):
    
    def __init__(self):
        super().__init__()
        self.resetear()
    
    def resetear(self):
        self.__torta = Torta()
    
    def crear_masa(self, masa):
        self.__torta.set_masa(masa)
        #self.__torta.masa = masa
    
    def crear_relleno(self, relleno):
        self.__torta.set_relleno(relleno)
        #self.__torta.relleno = relleno
    
    def get_torta (self):
        torta = self.__torta
        self.resetear()
        return torta