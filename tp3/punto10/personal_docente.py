from personal import Personal
class Personal_Docente (Personal):
    def __init__(self, nombre_empleado, antiguedad, sector, categoria):
        super().__init__(nombre_empleado, antiguedad, sector)
        self.__categoria_docente = categoria
    
    def calcula_horas_categoria (self):
        texto_mayusculado = self.__categoria_docente
        texto_mayusculado = texto_mayusculado.upper()
        if texto_mayusculado == "SIMPLE":
            return 10
        if texto_mayusculado == "SEMIEXCLUSIVA":
            return 20
        if texto_mayusculado == "EXCLUSIVA":
            return 40
        
    
    def imprimir_docente (self):
        print (f""" El DOCENTE {self.__str__} Tiene categoría {self.calcula_horas_categoria} por ende le corresponde {self.calcula_horas_categoria()} """)