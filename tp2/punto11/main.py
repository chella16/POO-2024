
from persona import Persona
from empresa import Empresa

trabaja = True
no_trabaja = False
estudia = True
no_estudia = False
m = "masculino"
f = "femenino"
lista_familias = []

empresa1 = Empresa("Panamerican Energy", "San martin 1945")
empleado1 = Persona(f, 56, trabaja, no_estudia)
empleado2 = Persona(m, 59, no_trabaja, no_estudia)
empleado3 = Persona(f, 20, no_trabaja, estudia)
empleado4 = Persona(m, 21, trabaja, estudia)
empleado5 = Persona(f, 20, trabaja, no_estudia)

empresa1.agregar_empleado(empleado1)
empresa1.agregar_empleado(empleado2)
empresa1.agregar_empleado(empleado3)
empresa1.agregar_empleado(empleado4)
empresa1.agregar_empleado(empleado5)

empresa2 = Empresa("PepeLore INC", "Rivadavia 943")
empleado1 = Persona(f, 47, trabaja, no_estudia)
empleado2 = Persona(m, 39, no_trabaja, no_estudia)
empleado3 = Persona(f, 60, no_trabaja, estudia)
empleado4 = Persona(m, 31, trabaja, estudia)
empleado5 = Persona(f, 0, trabaja, no_estudia)

empresa2.agregar_empleado(empleado1)
empresa2.agregar_empleado(empleado2)
empresa2.agregar_empleado(empleado3)
empresa2.agregar_empleado(empleado4)
#empresa2.agregar_empleado(empleado5)

empresa1.imprimir_info_empresa()
print(f"La cantidad de empleados que tiene la empresa es de {empresa1.cantidad_empleados()} negros de mierda")

empresa2.imprimir_info_empresa()
print(f"La cantidad de empleados que tiene la empresa es de {empresa2.cantidad_empleados()} negros de mierda")