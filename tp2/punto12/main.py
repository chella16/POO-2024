
from persona import Persona
from empresa import Empresa
from puesto import Puesto

m = "masculino"
f = "femenino"

Administrativo = Puesto("Administrativo")
Gerente = Puesto("Gerente")
Tesorero = Puesto("Tesorero")

empresa1 = Empresa("Panamerican Energy", "San martin 1945")
empleado1 = Persona(f, 56, Administrativo)
empleado2 = Persona(m, 59, Administrativo)
empleado3 = Persona(f, 20, Administrativo)
empleado4 = Persona(m, 21, Gerente)
empleado5 = Persona(f, 20, Tesorero)

empresa1.agregar_empleado(empleado1)
empresa1.agregar_empleado(empleado2)
empresa1.agregar_empleado(empleado3)
empresa1.agregar_empleado(empleado4)
empresa1.agregar_empleado(empleado5)

empresa2 = Empresa("PepeLore INC", "Rivadavia 943")
empleado1 = Persona(f, 47, Administrativo)
empleado2 = Persona(m, 39, Gerente)
empleado3 = Persona(f, 60, Tesorero)
empleado4 = Persona(m, 31, Tesorero)
empleado5 = Persona(f, 0, Administrativo)

empresa2.agregar_empleado(empleado1)
empresa2.agregar_empleado(empleado2)
empresa2.agregar_empleado(empleado3)
empresa2.agregar_empleado(empleado4)
#empresa2.agregar_empleado(empleado5)

empresa1.imprimir_info_empresa()
print(f"La cantidad de empleados que tiene la empresa es de {empresa1.cantidad_empleados()} negros de mierda")

empresa2.imprimir_info_empresa()
print(f"La cantidad de empleados que tiene la empresa es de {empresa2.cantidad_empleados()} negros de mierda")