
class Familia:
    
    def __init__(self, nombre_familia):
        self.__nombre_familia = nombre_familia 
        self.__integrantes = []
        
    def get_nombre_familia (self):
        return self.__nombre_familia
    
    def set_nombre_familia (self, nombre_familia):
        self.__nombre_familia = nombre_familia
    
    def agg_integrante(self, integrante):
        self.__integrantes.append(integrante)
    
    def imprimir(self):
        cont= 0
        print(f"la familia {self.__nombre_familia} está compuesta por:")
        for per in self.__integrantes:
            cont = cont + 1
            print(f" Integrante {cont} : {per.__str_persona__()}")