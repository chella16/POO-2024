from helpers import Helper_Tamaño_Letra, Helper_Traduccion
class Facade():
    
    def traduccion (s):
        palabra = Helper_Traduccion.traduccion_palabra(s)
        return palabra
    
    def mayuscula (s):
        palabra = Helper_Tamaño_Letra.mayusculizacion(s)
        return palabra
    
    def minuscula (s):
        palabra = Helper_Tamaño_Letra.minusculizacion(s)
        return palabra
