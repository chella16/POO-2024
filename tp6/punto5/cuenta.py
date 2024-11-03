#Desarrolla una clase Cuenta con un atributo saldo de tipo Float. Está representará a una
#cuenta bancaria y contendrá el monto monetario que se indique por defecto en el
#constructor.
#La clase debe poseer un método que permita descontar a ese saldo la cantidad
#indicada.
#Luego, cree una clase Tarjeta que extienda de Process y reciba en su constructor un
#número de identificación y una instancia de la clase Cuenta. Es decir, toda tarjeta estará
#asociada a una cuenta bancaria.
#Implemente el método run de tal manera que ejecute dos veces un descuento de saldo
#a la cuenta, a fines de prueba este descuento será siempre por $100.
#Cree una instancia de la clase Cuenta con un saldo de $2000. Cree diez instancias de
#la clase Tarjeta y asocie todas a la cuenta creada previamente. Ejecute el método start
#de cada instancia de tarjeta(las ejecuciones deben ser en paralelo)
#Al finalizar la ejecución de todos los procesos debe imprimirse el resultado. Este debería
#de ser cero. Valide ejecutando varias veces el programa asegura que no se obtiene un
#falso positivo
from multiprocessing import Value, Lock
class Cuenta ():
    def __init__(self):
        self._monto = Value('i', 2000)
    
    def descontar (self, monto, tarjeta, lock):
        montocuenta = self._monto
        with lock:
            if (montocuenta.value - monto) < 0:
                print("la cuenta dice que no hay fondos insuficientes para pagar", flush=True)
            else:
                    self._monto.value -= monto
                    print(f"Tarjeta: {tarjeta._id} Monto descontado a la cuenta: {monto}, saldo restante: {self._monto.value}", flush= True)
        
    def get_monto (self):
        return self._monto.value