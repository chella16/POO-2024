import threading

def imprimir_numeros():
    for i in range(1, 100):
        print(f'Número {i}')
    print("termina ejecución de imprimir_numeros")

def imprimir_letras():
    letras = 'ABCDEEFGHIJKLMNÑOPQRSTUVWXYZ'
    for letra in letras*5:
        print(f'Letra {letra}')
    print("termina ejecución de imprimir_letras")

thread1 = threading.Thread(target=imprimir_numeros)
thread2 = threading.Thread(target=imprimir_letras)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("termina ejecución de programa")
