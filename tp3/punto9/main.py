from claro import Claro
from personal import Personal
from movistar import Movistar
from random import randint

for i in range(4):
    if i == 1:
        gigas = randint (1,30)
        sms = randint (1,30)
        minutos = randint (1,30)
        tarifa_claro = Claro(sms, minutos, gigas)
    if i == 2:
        gigas = randint (1,30)
        sms = randint (1,30)
        minutos = randint (1,30)
        tarifa_personal = Personal(sms, minutos, gigas)
    if i == 3:
        gigas = randint (1,30)
        sms = randint (1,30)
        minutos = randint (1,30)
        tarifa_movistar = Movistar(sms, minutos, gigas)

print (tarifa_claro.__str__())
print (tarifa_personal.__str__())
print (tarifa_movistar.__str__())