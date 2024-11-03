from interfaz_juego import Juego

class Juego_Digital(Juego):
    
    def __init__(self, juego, importe, tarifa_pagina):
        super().__init__(juego, importe)
        self.__tarifa_pagina = tarifa_pagina
    
    def get_precio(self):
        precio = self._importe_juego * (1 + self.__tarifa_pagina)
        return precio
    
    def set_tarifa (self, tarifa):
        self.__tarifa_pagina = tarifa