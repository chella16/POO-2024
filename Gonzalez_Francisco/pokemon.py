from abc import ABC
from random import randint

class Pokemon(ABC):
    
    def __init__(self, nombre_pokemon):
        self._nombre_pokemon = nombre_pokemon
        self._tipo_pokemon = ""
        self._vida_pokemon = 100
        self._ataque_pokemon = randint (0,100)
        self._defensa_pokemon = randint (0,100)
        self._velocidad_pokemon = randint (0,100)
        self._debilidad = ""
        self._salvajismo_pokemon = randint (0,100)
    
    def get_salvajismo (self):
        return self._salvajismo_pokemon
    
    def set_salvajismo (self, salvajismo):
        self._salvajismo_pokemon = salvajismo
    
    def atacar_pokemon (self, pokemon_objetivo):
        debilidad_objetivo = pokemon_objetivo._debilidad
        debilidad_objetivo = debilidad_objetivo.upper()
        tipo_pokemon_atacante = self._tipo_pokemon
        tipo_pokemon_atacante = tipo_pokemon_atacante.upper()
        if debilidad_objetivo == tipo_pokemon_atacante:
            print (" El pokemon objetivo es debil!")
            probabilidad = randint(0,100)
            if probabilidad <= 70:
                ataque = self._ataque_pokemon * 1.5
                print (f"Ataque critico! {ataque}")
                return ataque
            else:
                ataque = self._ataque_pokemon
                print (f" Ataque normal {ataque}")
                return ataque
        else:
            print ("El pokemon objetivo no es debil")
            ataque = self._ataque_pokemon
            print (f" Ataque normal {ataque}")
            return ataque
    
    def defender_pokemon (self, daño_a_defender):
        pass
    
    def imprimir_info_pokemon (self):
        print(f""" {self._nombre_pokemon} - Es de tipo {self._tipo_pokemon} - Cuenta con:
            Nivel de ataque = {self._ataque_pokemon}
            Nivel de defensa = {self._ataque_pokemon}
            Velocidad = {self._velocidad_pokemon}
            Salvajismo = {self._salvajismo_pokemon}
            Debilidad = Pokemon tipo {self._debilidad}""")