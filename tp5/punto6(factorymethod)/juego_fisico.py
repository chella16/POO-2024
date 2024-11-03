from interfaz_juego import Juego
class Juego_Fisico(Juego):
    
    def __init__(self, juego, importe, envio):
        super().__init__(juego, importe)
        self.__precio_envio = envio
    
    def get_precio(self):
        precio = self._importe_juego + self.__precio_envio
        return precio
    
    def set_precio_envio (self, precio):
        self.__precio_envio = precio