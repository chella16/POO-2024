
class Entrenador():
    
    def __init__(self, nombre_entrenador, nivel, pokemon_principal) :
        self.__nombre_entrenador = nombre_entrenador
        self.__pokemon_principal = pokemon_principal
        self.__nivel_de_entrenador = nivel
        self.__pokedex = []
    
    def get_pokemon_prncipal (self):
        return self.__pokemon_principal.imprimir_info_pokemon()
    
    def atrapar_pokemon (self, pokemon_objetivo):
        print (f"{self.__nombre_entrenador}; Pokemon principal : {self.__pokemon_principal.imprimir_info_pokemon()}; Pokemon objetivo {pokemon_objetivo.imprimir_info_pokemon()}")
        atrapado = False
        for i in range(3):
            if pokemon_objetivo._vida_pokemon > 0 or self.__pokemon_principal._vida_pokemon > 0:
                print (f" Pokemon salvajismo {pokemon_objetivo._salvajismo_pokemon}; Ataque numero {i+1}")
                if self.__nivel_de_entrenador > pokemon_objetivo._salvajismo_pokemon and not atrapado:
                    self.__pokedex.append(pokemon_objetivo)
                    print("""Pokemon atrapado con éxito!
                        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
                    atrapado = True
                else:
                    ataque1 = self.__pokemon_principal.atacar_pokemon(pokemon_objetivo)
                    pokemon_objetivo.defender_pokemon(ataque1)
                    ataque2 = pokemon_objetivo.atacar_pokemon(self.__pokemon_principal)
                    self.__pokemon_principal.defender_pokemon(ataque2)
                    descuento = pokemon_objetivo._salvajismo_pokemon * 0.1
                    pokemon_objetivo._salvajismo_pokemon = pokemon_objetivo._salvajismo_pokemon - descuento # puede que haya un problema de setter o getter
                    print ("Salvajismo reducido un 10%")
            else:
                if pokemon_objetivo._vida_pokemon <= 0:
                    print ("El pokemon objetivo murió :(")
                if self.__pokemon_principal._vida_pokemon <= 0:
                    print ("El pokemon principal murió")
        self.__pokemon_principal._vida_pokemon = 100
    
    def imprimir_info_entrenador (self):
        print(f""" {self.__nombre_entrenador}; Nivel de entrenador = {self.__nivel_de_entrenador}
            Pokemon Principal {self.__pokemon_principal.imprimir_info_pokemon()}
            Pokedex = """)
        for i in self.__pokedex:
            i.imprimir_info_pokemon()
        
    