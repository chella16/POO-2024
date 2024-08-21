
from persona import Persona
from datetime import datetime

persona1 = Persona("Maximo", "Ortiz", datetime(2003,9,7))
persona2 = Persona("Joel", "Rodriguez", datetime(2003,12,13))
persona3 = Persona("Francisco","Gonzalez", datetime(2003,10,14))

print(persona1.__str__())
print(persona2.__str__())
print(persona3.__str__())
