from creador import Creador
from juego_fisico import Juego_Fisico
class Creador_Juego_Fisico (Creador):
    
    def crear_juego (id, precio, agregado):
        juego_fisico = Juego_Fisico (id, precio, agregado)
        #juego_fisico.set_precio_envio(agregado)
        return juego_fisico
    