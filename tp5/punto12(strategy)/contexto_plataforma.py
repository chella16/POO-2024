from abc import ABC
from estrategias import Strat_Completo
class Plataforma_streaming():
    
    def __init__(self, nombre):
        self.__estrategia = Strat_Completo()
        self.__catalogo_peliculas = []
        self.__nombre_plataforma = nombre
    
    def consultar_catalogo (self):
        print(f"Plataforma {self.__nombre_plataforma} : ")
        catalogo = self.__catalogo_peliculas
        self.__estrategia.consultar_catalogo(catalogo)
    
    def set_estrategia (self, estrategia):
        self.__estrategia = estrategia
    
    def get_estrategia (self):
        return self.__estrategia
    
    def agregar_pelicula (self, pelicula):
        self.__catalogo_peliculas.append(pelicula)
    
    def eliminar_pelicula (self, pelicula):
        self.__catalogo_peliculas.delete(pelicula)