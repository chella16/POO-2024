from contexto import Banco
from estado import Estado_Abierta, Estado_Suspendida
from persona import Persona

banco1 = Banco("CHUBUT")
banco2 = Banco("CROCANTE")
estado_suspendido = Estado_Suspendida()
estado_abierto = Estado_Abierta()

persona1 = Persona("Jacho", 61)
persona2 = Persona("Kanapka", 50)
persona3 = Persona("Pablin", 23)
persona4 = Persona("Cacorro", 60)

banco1.atender_personas(persona1)
banco2.atender_personas(persona1)
banco1.atender_personas(persona2)
banco2.atender_personas(persona2)
banco1.atender_personas(persona3)
banco2.atender_personas(persona3)
banco1.atender_personas(persona4)
banco2.atender_personas(persona4)

print ("Los bancos se estan poniendo en estado suspendido")
banco1.set_estado_banco(estado_suspendido)
banco2.set_estado_banco(estado_suspendido)

banco1.atender_personas(persona1)
banco2.atender_personas(persona1)
banco1.atender_personas(persona2)
banco2.atender_personas(persona2)
banco1.atender_personas(persona3)
banco2.atender_personas(persona3)
banco1.atender_personas(persona4)
banco2.atender_personas(persona4)

print ("Los bancos se estan abriendo!!")
banco1.set_estado_banco(estado_abierto)
banco2.set_estado_banco(estado_abierto)

banco1.atender_personas(persona1)
banco2.atender_personas(persona1)
banco1.atender_personas(persona2)
banco2.atender_personas(persona2)
banco1.atender_personas(persona3)
banco2.atender_personas(persona3)
banco1.atender_personas(persona4)
banco2.atender_personas(persona4)