from datetime import datetime
from random import randint
class Impuesto():
    
    def __init__(self, nombre, monto, periodo):
        self.__nombre = nombre
        self.__monto = monto
        self.__periodo = periodo
        self.__estado = "Pendiente"
        self.__comprobante = 0
        
    def genera_comprobante (self, nro):
        self.__comprobante = nro
    
    def validacion_pago (self, cuenta, tipo_pago, cantidad_cuotas, fecha_pago):
        saldo = cuenta._saldo_cuenta
        if tipo_pago == 1:
            cuenta.pago_con_debito(self.__monto)
            if self.__monto != saldo:
                print("pago realizadooo")
                self.__estado = "Pagado"
                nro = randint(1000000, 9999999)
                self.genera_comprobante(nro)
                mes = fecha_pago.month
            if self.__periodo.month == mes:
                print(" el pago corresponde al mes corriente ")
            else:
                print ("el pago no corresponde a este més")
        else:
            cuenta.pago_con_credito(self.__monto, cantidad_cuotas)
            if self.__monto != saldo:
                print("pago realizadooo")
                self.__estado = "Pagado"
                nro = randint(1000000, 9999999)
                self.genera_comprobante(nro)
                mes = fecha_pago.month
            if self.__periodo.month == mes :
                print(" el pago corresponde al mes corriente ")
            else:
                print ("el pago no corresponde a este més")
        print (cuenta.__str__)
        
    def __str__(self) :
        return (f"El impuesto {self.__nombre}, con el monto {self.__monto}, del periodo {self.__periodo}, está {self.__estado}, por eso su comprobante es {self.__comprobante}")
    