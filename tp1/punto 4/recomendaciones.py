

class Recomendaciones:
    # aca deberia haber titulo tipo string
    def __init__(self, titulo) -> None:
        self.__titulo = titulo
        self.__cursos = []
    
    def agregar_curso(self, curso):
        self.__cursos.append(curso)
        
    def imprimir (self):
        print(self.__titulo)
        for cacamate in self.__cursos:
            cacamate.imprimir()
            
    