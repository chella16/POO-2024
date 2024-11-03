from cuenta import Cuenta
class Cuenta_Banco (Cuenta):
    
    def __init__(self, saldo, dueño, nro, nro_cbu, fecha_pago):
        super().__init__(saldo, dueño, nro, fecha_pago)
        self.__cbu = nro_cbu
    
    def pago_con_credito(self, monto, cantidad_cuotas):
        interes = 0
        if cantidad_cuotas <= 3:
            monto = monto / cantidad_cuotas
            if self._saldo_cuenta < monto:
                print (" NO HAY PLATA POBRE ")
            else: 
                self._saldo_cuenta = self._saldo_cuenta - monto
                print (" SALDO PAGADO, en menos de 3 cuotas con credito en cuenta de banco")
        else:
            interes = ((cantidad_cuotas * 2) / 100) + 1
            monto = (monto / cantidad_cuotas) * interes
            if self._saldo_cuenta < monto:
                print (" NO HAY PLATA POBRE ")
            else: 
                self._saldo_cuenta = self._saldo_cuenta - monto
                print (" SALDO PAGADO, en mas de 3 cuotas con credito en cuenta de banco")
        return monto
    
    def __str__(self):
        return f"Cuenta bancaria de CBU {self.__cbu} {super().__str__()}"