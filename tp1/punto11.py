
from random import random, randint, uniform

def valor_valido (cade):
    try:
        int(cade)
        return True
    except ValueError:
        print("tipo de dato erroneo ")
        return False


rta = "si"
ganadas = 0
perdidas = 0
while rta == "si":
    nro1 = randint(1,20)
    nro2 = randint(1,20)
    if nro1 != nro2:
        pick = input ("aposta por cual de los 2 numeros generados por la compu es mayor, el 1 o el 2 ")
        if valor_valido(pick):
            pick = int(pick)
            if pick == 1:
                if nro1 > nro2:
                    ganadas = ganadas + 1
                    print("ganaste paa ")
                else:
                    perdidas = perdidas + 1
                    print("perdiste bot ")
            elif pick == 2:
                if nro2 > nro1:
                    ganadas = ganadas + 1
                    print("ganaste paa ")
                else:
                    perdidas = perdidas + 1
                    print("perdiste bot ")
            else:
                print("pickeaste pura mierda gil ")
    print(f"estos fueron los valores: nro1 = {nro1}  nro2 = {nro2} ")
    rta = input("queres volver a apostar, si o no? ")

print(f"la cantidad de partidas que ganaste es {ganadas} ")
print(f"la cantidad de partidas que perdiste es {perdidas} ")