from personaje import Personaje
from valor_negativo import Valor_Negativo
class Bueno (Personaje):
    
    def __init__(self, nivel_ataque, nivel_defensa):
        super().__init__(290 , nivel_ataque, nivel_defensa)
    
    def defender(self, ataque):
        ataque = ataque - self._nivel_defensa
        self._vida = self._vida - ataque
        return ataque
    