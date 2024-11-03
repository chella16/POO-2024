import multiprocessing
from random import randint

def sumatoria(args):
    lista1, lista2 = args  # Desempaquetamos los argumentos
    sumatoria = 0
    for i in range(len(lista1)):
        num1 = lista1[i]
        num2 = lista2[i]
        sumatoria += num1 + num2
    return sumatoria

if __name__ == '__main__':
    mat1 = []
    mat2 = []
    
    for j in range(5):
        lista = []
        for i in range(5):
            numran = randint(10, 70)
            lista.append(numran)
        mat1.append(lista)
    
    for j in range(5):
        lista = []
        for i in range(5):
            numran = randint(10, 70)
            lista.append(numran)
        mat2.append(lista)
    
    print("matriz1:", mat1)
    print("matriz2:", mat2)
    
    with multiprocessing.Pool(processes=5) as pool:
        # Creamos una lista de tuplas, cada tupla contiene una fila de mat1 y la correspondiente de mat2
        argumentos = list(zip(mat1, mat2))
        resultados = pool.map(sumatoria, argumentos)
    
    print("Resultado Final de Sumatoria:", resultados)
