from malo import Malo
from bueno import Bueno
from valor_negativo import Valor_Negativo

pj1 = Bueno(25, 20)
pj2 = Malo(40, 5)

while pj1._vida > 0:
    try:
        print(pj1.__str__())
        print (pj2.__str__())
        print ("atacandooo!!")
        ataquemalo = pj2.atacar()
        print (f"ataque aumentado a: {ataquemalo}")
        pj1.defender(ataquemalo)
    except Valor_Negativo as e:
        print(f"dejá de pegarle gil , ya murio: {e}")
    finally:
        print (" ataque terminadoo ! ")
        print(pj1.__str__())
        print (pj2.__str__())
