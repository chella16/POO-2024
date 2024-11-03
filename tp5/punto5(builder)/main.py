from constructor_torta import Constructor_Torta
from director import Director

director = Director()

constructor = Constructor_Torta()
director.construccion_torta_vainilla(constructor)
torta_vainilla = constructor.get_torta()

director.construccion_torta_coco(constructor)
torta_coco = constructor.get_torta()

director.construccion_chocotorta(constructor)
chocotorta = constructor.get_torta()


torta_vainilla.mostrar_torta()
torta_coco.mostrar_torta()
chocotorta.mostrar_torta()