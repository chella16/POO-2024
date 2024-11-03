from observable import Sistema_meteorologico
from observers import Reportero

sist = Sistema_meteorologico()
reportero1 = Reportero()
reportero2 = Reportero()

sist.agregar_subs(reportero1)

sist.detectar_cambio_estado()

sist.agregar_subs(reportero2)

sist.detectar_cambio_estado()

sist.eliminar_subs(reportero1)

sist.detectar_cambio_estado()

sist.eliminar_subs(reportero2)

sist.detectar_cambio_estado()