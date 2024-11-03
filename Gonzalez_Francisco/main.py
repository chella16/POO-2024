from pokemon_hierba import Pokemon_Hierba
from pokemon_fuego import Pokemon_Fuego
from pokemon_agua import Pokemon_Agua
from entrenador import Entrenador
from random import randint

Lista_pokemones_salvajes = []

nro= randint(1,3)
nivel_entrenador = randint(1,100)
nombre = "Pokemon_principal_entrenador"
if nro == 1:
    pokemon = Pokemon_Hierba(nombre)
if nro == 2:
    pokemon = Pokemon_Fuego(nombre)
if nro ==3 :
    pokemon = Pokemon_Agua(nombre)
Entrenador_random = Entrenador("Pablo",nivel_entrenador, pokemon)

for i in range(10):
    nombre = f"Pokemon{i+1}"
    nro = randint(1,3)
    if nro == 1:
        pokemon = Pokemon_Hierba(nombre)
        Lista_pokemones_salvajes.append(pokemon)
    if nro == 2:
        pokemon = Pokemon_Fuego(nombre)
        Lista_pokemones_salvajes.append(pokemon)
    if nro ==3:
        pokemon = Pokemon_Agua(nombre)
        Lista_pokemones_salvajes.append(pokemon)

for i in Lista_pokemones_salvajes:
    Entrenador_random.atrapar_pokemon(i)

Entrenador_random.imprimir_info_entrenador()