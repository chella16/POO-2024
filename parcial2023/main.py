from cuenta_banco import Cuenta_Banco
from billetera_virtual import Billetera_Virtual
from impuesto import Impuesto
from random import randint
from datetime import datetime

for i in range(22):
    saldo = randint (10000, 30000)
    dueño = f"dueño {i}"
    nro_cuenta = randint (10000000, 99999999)
    cbvu = randint(100000000000, 999999999999)
    fecha_pago = datetime.now()
    if i == 1:
        targeta_banco = Cuenta_Banco(saldo, dueño, nro_cuenta, cbvu,  fecha_pago)
    else :
        targeta_virtual = Billetera_Virtual(saldo, dueño, nro_cuenta, cbvu, fecha_pago)

impuestos=[]
for i in range(20):
    nombre = f"impuesto{i}"
    monto = randint (1000, 5000)
    año = randint(2023,2024)
    mes = randint(1,12)
    dia = randint(1,29)
    periodo = datetime(año, mes, dia)
    impuesto = Impuesto (nombre, monto, periodo)
    impuestos.append(impuesto)

for i in impuestos:
    cuenta = randint(1,2)
    tipo_pago = randint(1,2)
    if cuenta == 1:
        if tipo_pago == 1:
            i.validacion_pago(targeta_virtual, tipo_pago, 0, fecha_pago)
        else:
            cantidad_cuotas= randint(1,12)
            i.validacion_pago(targeta_virtual, tipo_pago, cantidad_cuotas, fecha_pago)
    else:
        if tipo_pago == 1:
            i.validacion_pago(targeta_banco, tipo_pago, 0, fecha_pago)
        else:
            cantidad_cuotas= randint(1,12)
            i.validacion_pago(targeta_banco, tipo_pago, cantidad_cuotas, fecha_pago)
    print(i.__str__)
    
    