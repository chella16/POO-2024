from pokemon import Pokemon

class Pokemon_Fuego (Pokemon):
    
    def __init__(self, nombre_pokemon):
        super().__init__(nombre_pokemon)
        self._tipo_pokemon = "Fuego"
        self._debilidad = "Agua"
    
    def get_tipo_pokemon (self):
        return self._tipo_pokemon
    
    def get_debilidad (self):
        return self._debilidad
    
    def defender_pokemon(self, daño_a_defender):
        if self._defensa_pokemon <= daño_a_defender:
            daño_a_defender = daño_a_defender - self._defensa_pokemon
            self._vida_pokemon = self._vida_pokemon - daño_a_defender
            print (f""" Daño defendido !,  Daño inflijido = {daño_a_defender}, Vida restanto = {self._vida_pokemon}
                ------------------------------------""")
        else :
            print("""Ataque completamente reducido
                ------------------------------------""")
