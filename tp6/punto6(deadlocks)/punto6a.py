from multiprocessing import Process
from multiprocessing import Lock, RLock

#def task(lock):
    #print('Adquiriendo el lock...', flush=True)
    #with lock:
        #print('Adquiriendo el lock otra vez...', flush=True)
        #with lock:
            #pass


def task(lock):
    marca = True
    print('Adquiriendo el lock...', flush=True)
    lock.acquire()
    if marca:
        print('Adquiriendo el lock otra vez...', flush=True)
        lock.acquire()
        if marca:
            pass
    print('Liberando el lock 1 vez', flush=True)
    lock.release() # esto es para liberar de manera eficiente los recursos de la computadora
    print('Liberando el 2do lock', flush=True)
    lock.release()

#if __name__ == '__main__':
    #lock = Lock()
    #process = Process(target=task, args=(lock,))
    #process.start()
    #process.join()

if __name__ == '__main__':
    lock = RLock()
    process = Process(target=task, args=(lock,))
    process.start()
    process.join()

#Creo que el deadlock en este caso lo causa el hecho de que el bloque de task intenta adquirir el mismo bloqueo 2 veces, si
#fuera necesario yo creo que deberia adquirir 2 locks distintos para solucionarlo de manera definitiva, sino se deberia utitlizar
# un reentrant mutex lock, que es un tipo de bloqueo que permite ser adquirido más de una vez en el mismo hilo o proceso sin
#quedar en un deadlock 
