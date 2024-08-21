
from curso import Curso
from recomendaciones import Recomendaciones

curso1 = Curso("imagen curso1", "curso python" , "dictado por tomas latiza" , "4.8 / 5" , "59 USD" , "best seller nashe")
curso2 = Curso("imagen curso2", "curso de sexongus" , "dictado por martin garabal 2018" , "3.7 / 5" , "10 USD", "hot & new")
curso3 = Curso("imagen curso3", "curso de almohadas de pluma" , "dictado por chimchong chung" , "4.2 / 5" , "15 USD", "low cost")
recomendacion = Recomendaciones ("para vos...")
recomendacion.agregar_curso(curso1)
recomendacion.agregar_curso(curso2)
recomendacion.agregar_curso(curso3)
recomendacion.imprimir()