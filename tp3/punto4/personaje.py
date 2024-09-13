from abc import ABC, abstractmethod
from valor_negativo import Valor_Negativo

class Personaje (ABC):
    
    def __init__(self, vida, nivel_ataque, nivel_defensa):
        self._vida = vida
        self._nivel_ataque = nivel_ataque
        self._nivel_defensa = nivel_defensa
    
    def set_vida (self, vida):
        self._vida = vida
    
    def get_vida (self):
        return self._vida
    
    def set_nivel_ataque (self, nivel_ataque):
        self._nivel_ataque = nivel_ataque
    
    def get_nivel_ataque (self):
        return self._nivel_ataque
    
    def set_nivel_defensa (self, nivel_defensa):
        self._nivel_defensa = nivel_defensa
    
    def get_nivel_defensa (self):
        return self._nivel_defensa
    
    def atacar (self):
        return 10
    
    @abstractmethod
    def defender (ataque):
        pass
    
    def __str__(self) :
        return (f" Vida del pj = {self._vida}; Nivel de defensa = {self._nivel_defensa}; Nivel de ataque = {self._nivel_ataque}")
