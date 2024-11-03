from multiprocessing import parent_process, current_process, Process

def task():
    current = current_process()
    parent = parent_process()
    print(f'[{current.name}] esperando a [{parent.name}]...', flush=True)
    parent.join()

if __name__ == '__main__':
    current = current_process()
    child = Process(target=task)
    child.start()
    print(f'[{current.name}] esperando a [{child.name}]...', flush=True)
    child.join()

#Este bloqueo se debe a que el proceso principal dice que esta esperando a que termine el proceso1 y a su vez el proceso 1 dice
#que esta esperando a que el proceso padre termine y resulta en un bloqueo infinito que nunca termina. este tipo de bloqueo
#no tiene solucion más que gestionar bien los recurssos que necesita cada proceso para poder seguir su curso XD
