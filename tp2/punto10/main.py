
from familia import Familia
from persona import Persona

trabaja = True
no_trabaja = False
estudia = True
no_estudia = False
m = "masculino"
f = "femenino"
lista_familias = []

familia1 = Familia("Gonzalez")
integrante1 = Persona("f", 56, trabaja, estudia)
integrante2 = Persona("m", 59, no_trabaja, no_estudia)
integrante3 = Persona("m", 20, no_trabaja, estudia)
familia1.agg_integrante(integrante1)
familia1.agg_integrante(integrante2)
familia1.agg_integrante(integrante3)
lista_familias.append(familia1)

familia2 = Familia("Ortiz")
integrante1 = Persona("f", 50, no_trabaja, no_estudia)
integrante2 = Persona("m", 48, trabaja, no_estudia)
integrante3 = Persona("m", 20, no_trabaja, no_estudia)
integrante4 = Persona("f", 15, no_trabaja, estudia)
familia2.agg_integrante(integrante1)
familia2.agg_integrante(integrante2)
familia2.agg_integrante(integrante3)
familia2.agg_integrante(integrante4)
lista_familias.append(familia2)

familia1.imprimir()
familia2.imprimir()
cantidad_familias = 0
cantidad_integrantes = 0
promedio_edades = 0
trabajadores = 0

for family in lista_familias:
    cantidad_familias = cantidad_familias + 1
    cantidad_integrantes = cantidad_integrantes + family.cuenta_personas()
    promedio_edades = promedio_edades + family.acumulador_edad()
    trabajadores = trabajadores + family.cuenta_trabajadores()

promedio_edades = promedio_edades / cantidad_integrantes

print(f"La cantidad de familias censadas es: {cantidad_familias} La cantida de personas censadas fue de: {cantidad_integrantes}")
print(f"El promedio de edad es de {promedio_edades}. Siendo las personas que trabajan un total de {trabajadores}")
