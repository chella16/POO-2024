from creador import Creador
from juego_digital import Juego_Digital
class Creador_Juego_Digital(Creador):
    
    def crear_juego( id, precio, agregado):
        juego_digital = Juego_Digital(id, precio, agregado)
        #juego_digital.set_tarifa(agregado)
        return juego_digital