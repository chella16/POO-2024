from abc import ABC
class Estrategia_Interfaz (ABC):
    
    def consultar_catalogo(self,catalogo):
        pass

class Strat_Menores_13 (Estrategia_Interfaz):
    
    def consultar_catalogo(self, catalogo):
        print ("Peliculas para MENORES DE 13")
        for pelicula in catalogo:
            if pelicula.get_clasificacion() < 13:
                print (" " * 4 + f"{pelicula.get_nombre()} Pelicula para mayores de {pelicula.get_clasificacion()}")

class Strat_Completo (Estrategia_Interfaz):
    
    def consultar_catalogo(self, catalogo):
        print ("Catalogo COMPLETO de peliculas")
        for pelicula in catalogo:
            print (" " * 4 + f"{pelicula.get_nombre()} Pelicula para mayores de {pelicula.get_clasificacion()}")

class Strat_Menores_18 (Estrategia_Interfaz):
    
    def consultar_catalogo(self, catalogo):
        print ("Peliculas para MENORES DE 18")
        for pelicula in catalogo:
            if pelicula.get_clasificacion() < 18:
                print (" " * 4 + f"{pelicula.get_nombre()} Pelicula para mayores de {pelicula.get_clasificacion()}")