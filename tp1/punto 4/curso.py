


class Curso:
    def __init__(self, imagen, titulo, descripcion, rating, precio, categoria) -> None:
        self.__image = imagen
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__rating = rating
        self.__precio = precio
        self.__categoria = categoria

def imprimir (self):
    print ("{} {} {}".format(self.__image, self.__titulo, self.__descripcion, self.__rating, self.__precio, self.__categoria) )
