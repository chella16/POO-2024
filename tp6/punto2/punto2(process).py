from multiprocessing import Process, Value

class Contador_Numero(Process):
    
    
    def incrementar (variable_compartida):
        for i in range(5000):
            with variable_compartida.get_lock():
                variable_compartida.value += 1

if __name__ == '__main__':
    var_comp = Value('i', 0)

    proceso1 = Process(target=Contador_Numero.incrementar, args=(var_comp,))
    print(f"El proceso {proceso1.name} incrementó la variable nashe")
    proceso2 = Process(target=Contador_Numero.incrementar, args=(var_comp,))
    print(f"El proceso {proceso2.name} incrementó la variable nashe")
    proceso3 = Process(target=Contador_Numero.incrementar, args=(var_comp,))
    print(f"El proceso {proceso3.name} incrementó la variable nashe")
    proceso4 = Process(target=Contador_Numero.incrementar, args=(var_comp,))
    print(f"El proceso {proceso4.name} incrementó la variable nashe")

    proceso1.start()
    proceso2.start()
    proceso3.start()
    proceso4.start()

    proceso1.join()
    proceso2.join()
    proceso3.join()
    proceso4.join()

    print ("el valor final de la variable es: ", var_comp.value)
    