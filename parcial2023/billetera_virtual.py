from cuenta import Cuenta
class Billetera_Virtual (Cuenta):
    
    def __init__(self, saldo, dueño, nro, cvu, fecha_pago):
        super().__init__(saldo, dueño, nro, fecha_pago)
        self.__nro_cvu = cvu
    
    def pago_con_credito(self, monto, cantidad_cuotas):
        interes = cantidad_cuotas * 0.08
        interes = interes + 1
        monto = (monto / cantidad_cuotas) * interes
        self._saldo_cuenta = self._saldo_cuenta - monto
        print (f"SALDO PAGADO, en {cantidad_cuotas} Cuotas con credito en billetera virtual")
        return monto
    
    