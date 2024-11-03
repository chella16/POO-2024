from multiprocessing import Process
from multiprocessing import Lock

def task(lock):
    print('Adquiriendo el lock...', flush=True)
    with lock:
        print('Adquiriendo el lock otra vez...', flush=True)
        with lock:
            pass

if __name__ == '__main__':
    lock = Lock()
    process = Process(target=task, args=(lock,))
    process.start()
    process.join()
