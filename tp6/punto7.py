#Dado el escenario en el cual se encuentran dos personas intentando comer sopa pero
#se encuentran con que solo tienen una cuchara para hacerlo. ¿Qué tipo de problema
#con hilos se produce? ¿Cómo se resolvería?

#Yo creo que ese enunciado produce un error de tipo deadlock ya que ambos comensales etarian esperando el mismo recurso para 
# comer (la cuchara) y se estarian bloqueando mutuamente ya que es un recurso que ambos necesitan para comer y no deberia ser 
# compartido por lo que la solucion podria ser que uno bloquee su curso de accion mientras el otro come, y que una vez comió
# libere el recurso así el otro comensal

