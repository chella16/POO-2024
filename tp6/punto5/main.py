#Cree una instancia de la clase Cuenta con un saldo de $2000. Cree diez instancias de
#la clase Tarjeta y asocie todas a la cuenta creada previamente. Ejecute el método start
#de cada instancia de tarjeta(las ejecuciones deben ser en paralelo)
#Al finalizar la ejecución de todos los procesos debe imprimirse el resultado. Este debería
#de ser cero. Valide ejecutando varias veces el programa asegura que no se obtiene un
#falso positivo
from cuenta import Cuenta
from tarjeta import Tarjeta

if __name__ == '__main__':
    cuenta_main = Cuenta()
    tarjeta1 = Tarjeta(1, cuenta_main)
    tarjeta2 = Tarjeta(2, cuenta_main)
    tarjeta3 = Tarjeta(3, cuenta_main)
    tarjeta4 = Tarjeta(4, cuenta_main)
    tarjeta5 = Tarjeta(5, cuenta_main)
    tarjeta6 = Tarjeta(6, cuenta_main)
    tarjeta7 = Tarjeta(7, cuenta_main)
    tarjeta8 = Tarjeta(8, cuenta_main)
    tarjeta9 = Tarjeta(9, cuenta_main)
    tarjeta10 = Tarjeta(10, cuenta_main)
    tarjeta11 = Tarjeta(10, cuenta_main)

    tarjeta1.start()
    tarjeta2.start()
    tarjeta3.start()
    tarjeta4.start()
    tarjeta5.start()
    tarjeta6.start()
    tarjeta7.start()
    tarjeta8.start()
    tarjeta9.start()
    tarjeta10.start()
    tarjeta11.start()

    tarjeta1.join()
    tarjeta2.join()
    tarjeta3.join()
    tarjeta4.join()
    tarjeta5.join()
    tarjeta6.join()
    tarjeta7.join()
    tarjeta8.join()
    tarjeta9.join()
    tarjeta10.join()
    tarjeta11.join()

    print (f"EL RESULTADO FINAL DE TODAS LAS TRANSACCIONES DEJó Un SALDO DE: {cuenta_main.get_monto()}")