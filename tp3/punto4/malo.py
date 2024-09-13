from personaje import Personaje
from valor_negativo import Valor_Negativo
class Malo(Personaje):
    
    def __init__(self, nivel_ataque, nivel_defensa):
        super().__init__(200, nivel_ataque, nivel_defensa)
    
    def defender(self, ataque):
        ataque = ataque - self._nivel_defensa
        self._vida = self._vida - ataque
        return f"Ataque final = {ataque}, Vida restante = {self._vida} "
    
    def atacar(self):
        ataque = super().atacar()
        ataque = ataque + self._nivel_ataque
        return ataque
        
    
    # si no ponia el super estoy sobreescribiendo el metodo en lugar de extenderlo