
class Torta ():
    
    def __init__(self):
        self.__masa =""
        self.__relleno = ""
    
    def set_relleno (self, relleno):
        self.__relleno = relleno
    
    def set_masa (self, masa):
        self.__masa = masa
    
    def mostrar_torta (self):
        print(f" esta torta contiene una masa : {self.__masa} y contiene un relleno: {self.__relleno}")