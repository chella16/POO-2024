
from random import randint, random, uniform
nro_random = randint(1,10)
nro_pickeado = int(input(" ingresa el numero pa "))
if nro_pickeado > nro_random:
    print(f"{nro_pickeado} es mayor a {nro_random}")
elif nro_pickeado < nro_random:
    print(f"{nro_pickeado} es menor a {nro_random}")
else:
    print(f"{nro_pickeado} es igual a {nro_random}")
