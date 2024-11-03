from carpeta_composite import Carpeta
from archivo_hoja import Archivo

carpeta1 = Carpeta("Carpeta1")
carpeta2 = Carpeta("Carpeta2")
carpeta3 = Carpeta("Carpeta3")

archivo1 = Archivo("Archivo1")
archivo2 = Archivo("Archivo2")
archivo3 = Archivo("Archivo3")
archivo4 = Archivo("Archivo4")

carpeta2.agregar_componente(archivo1)
carpeta2.agregar_componente(archivo2)

carpeta1.agregar_componente(carpeta2)
carpeta1.agregar_componente(archivo3)

carpeta3.agregar_componente(archivo4)

carpeta_madre = Carpeta("Carpeta Madre")

carpeta_madre.agregar_componente(carpeta1)
carpeta_madre.agregar_componente(carpeta3)

carpeta_madre.imprimir_contenido()