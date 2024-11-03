from pokemon import Pokemon
from random import randint

class Pokemon_Agua (Pokemon):
    
    def __init__(self, nombre_pokemon):
        super().__init__(nombre_pokemon)
        self._tipo_pokemon = "Agua"
        self._debilidad = "Hierba"
    
    def atacar_pokemon(self, pokemon_objetivo):
        debilidad_objetivo = pokemon_objetivo._debilidad
        debilidad_objetivo = debilidad_objetivo.upper()
        tipo_pokemon_atacante = self._tipo_pokemon
        tipo_pokemon_atacante = tipo_pokemon_atacante.upper()
        if debilidad_objetivo == tipo_pokemon_atacante:
            print (" El pokemon objetivo es debil! Aumentando ataque...")
            ataque = self._ataque_pokemon * 1.7
            print (f"Ataque critico! {ataque}")
            return ataque
        else:
            print (" El pokemon objetivo no es debil ")
            print (f" Ataque normal {self._ataque_pokemon}")
            return self._ataque_pokemon
        
    def defender_pokemon(self, daño_a_defender):
        if self._defensa_pokemon <= daño_a_defender:
            probabilidad = randint(1,30)
            if probabilidad < 30:
                daño_a_defender = daño_a_defender * 0.5
                print (f""" Ataque reducido a la mitad! Daño inflijido = {daño_a_defender} ; Nivel de vida restante = {self._vida_pokemon}
                    ------------------------------------""")
                self._vida_pokemon = self._vida_pokemon - daño_a_defender
            else:
                print (f"""No se pudo reducir el daño a la mitad, Daño inflijido = {daño_a_defender} ; Nivel de vida restante = {self._vida_pokemon}
                    ------------------------------------""")
                self._vida_pokemon = self._vida_pokemon - daño_a_defender
        else:
            print("""Ataque completamente reducido
                ------------------------------------""")
    