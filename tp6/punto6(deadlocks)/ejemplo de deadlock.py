from multiprocessing import Process, Lock
import time

def task1(lock1, lock2):
    with lock1:
        print("Proceso 1: Adquirió lock1")
        time.sleep(1)  # Simula trabajo
        with lock2:
            print("Proceso 1: Adquirió lock2")

def task2(lock1, lock2):
    with lock2:
        print("Proceso 2: Adquirió lock2")
        time.sleep(1)  # Simula trabajo
        with lock1:
            print("Proceso 2: Adquirió lock1")

if __name__ == "__main__":
    lock1 = Lock()
    lock2 = Lock()

    p1 = Process(target=task1, args=(lock1, lock2))
    p2 = Process(target=task2, args=(lock1, lock2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()