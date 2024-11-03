#Implemente un programa que escriba un “hola mundo” por 
#cada hilo de ejecución que se cree
#(seis es un número razonable) y que además indique
# desde qué hilo se imprime. Luego haga que cada uno 
#espere un tiempo proporcional a su identificador
#antes de imprimir el mensaje (el thread 1, un segundo,
#el 2, dos segundos, el 3, tres segundos).
from threading import Thread
import threading
import time

class Hola_Mundo(Thread):

    def imprimir_hola_mundo (self, tiempo):
        time.sleep(tiempo)
        print (f"HOLA MUNDITO desde el hilo: {self.name }")
    
for i in range (1,7):
    Hola_Mundo().imprimir_hola_mundo(i)

