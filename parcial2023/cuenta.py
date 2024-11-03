
class Cuenta ():
    
    def __init__(self, saldo, dueño, nro, fecha_pago) :
        self._saldo_cuenta = saldo
        self._dueño_cuenta = dueño
        self._nro_cuenta = nro
    
    def pago_con_debito (self, monto):
        if self._saldo_cuenta < monto:
                print (" NO HAY PLATA POBRE ")
        else: 
            self._saldo_cuenta = self._saldo_cuenta - monto
            self._saldo_cuenta = self._saldo_cuenta + (0.1 * monto)
            print (" SALDO PAGADO CON DEBITO ")
    
    def pago_con_credito (self,monto, cantidad_cuotas):
        pass
    
    def get_saldo (self):
        return self._saldo_cuenta
    
    def __str__(self) :
        return (f"NUMERO DE CUENTA {self._nro_cuenta}; del DUEÑO {self._dueño_cuenta}; cuenta con un SALDO de: {self._saldo_cuenta}")