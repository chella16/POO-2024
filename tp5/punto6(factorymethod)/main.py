from creador import Creador
from creador_juego_digital import Creador_Juego_Digital
from creador_juego_fisico import Creador_Juego_Fisico
from juego_fisico import Juego_Fisico
from juego_digital import Juego_Digital



print("CREANDO UN JUEGO DIGITAL PARA STEAM QUE SALE 7 dolaresss sin incluir tarifas extra")
paunch = Creador_Juego_Digital.crear_juego("Paunch God", 7, 0.33)
print ("CREANDO UN JUEGAZO FISICO QUE SALE 700 pesos Y PREPARANDO EL ENVIO HASTA CR pa")
gta_sa = Creador_Juego_Fisico.crear_juego("G.T.A San Andreas", 700, 200)

print (f"El Paunch tiene un precio total final de {paunch.get_precio()} dolares en Steam")
print (f"El GTA San Andreas tiene un precio final con envio hasta CR de {gta_sa.get_precio()}")

