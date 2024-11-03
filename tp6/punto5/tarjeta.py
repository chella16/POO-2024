#Luego, cree una clase Tarjeta que extienda de Process y reciba en su constructor un
#número de identificación y una instancia de la clase Cuenta. Es decir, toda tarjeta estará
#asociada a una cuenta bancaria.
#Implemente el método run de tal manera que ejecute dos veces un descuento de saldo
#a la cuenta, a fines de prueba este descuento será siempre por $100.

from multiprocessing import Process, Lock
class Tarjeta (Process):
    
    def __init__(self, id, cuenta):
        super().__init__()
        self._id = id
        self._cuenta = cuenta
    
    def run (self):
        lock = Lock()
        self._cuenta.descontar(100, self, lock)
        self._cuenta.descontar(100, self, lock)