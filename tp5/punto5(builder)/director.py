from constructor_torta import Constructor_Torta
class Director():
    def __init__(self):
        self.__constructor = None
    
    def set_constructor (self, constructor):
        self.__constructor = constructor
    
    def construccion_torta_vainilla (self, constructor):
        constructor.resetear()
        masa_vainilla = "Masa de Vainilla"
        constructor.crear_masa(masa_vainilla)
        relleno_vainilla = "Relleno de Vainilla"
        constructor.crear_relleno(relleno_vainilla)
    
    def construccion_torta_coco (self, constructor):
        constructor.resetear()
        constructor.crear_masa("Masa de coco")
        constructor.crear_relleno("Relleno de Coco")
    
    def construccion_chocotorta (self, constructor):
        constructor.resetear()
        constructor.crear_masa("Chocolinas")
        constructor.crear_relleno("Relleno de dulce de leche repostero y queso crema")
    

#cabe aclarar que esto implica que cadad construccion tenga mas pasos o menos y que los pasos
#difieran de una construccion a otra XD esa es la gracia de este patron