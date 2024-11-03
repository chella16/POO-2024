from pokemon import Pokemon
from random import randint

class Pokemon_Hierba(Pokemon):
    
    def __init__(self, nombre_pokemon):
        super().__init__(nombre_pokemon)
        self._tipo_pokemon = "Hierba"
        self._debilidad = "Fuego"
    
    def get_tipo_pokemon (self):
        return self._tipo_pokemon
    
    def get_debilidad (self):
        return self._debilidad
    
    def defender_pokemon(self, daño_a_defender):
        if self._defensa_pokemon <= daño_a_defender:
            if self._velocidad_pokemon > 50:
                probabilidad = randint(1,50)
                if probabilidad < 50:
                    daño_a_defender = daño_a_defender - self._defensa_pokemon
                    self._vida_pokemon = self._vida_pokemon - daño_a_defender
                    print (f"""Ataque reducido con exito!, Daño inflijido = {daño_a_defender}, Nivel de vida restante = {self._vida_pokemon}
                        ------------------------------------""")
                else:
                    self._vida_pokemon = self._vida_pokemon - daño_a_defender
                    print(f"""El Ataque no pudo ser reducido, Daño inflijido = {daño_a_defender}, Nivel de vida restante = {self._vida_pokemon}
                        ------------------------------------""")
        else:
            print("""Ataque defendido por completo
                ------------------------------------""")
            
    