from abc import ABC
class Juego(ABC):
    
    def __init__(self, juego, importe):
        self._id_juego = juego
        self._importe_juego = importe
    
    def get_precio (self):
        pass