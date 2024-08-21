from Serie import Serie
from Categoria import Categoria

serie = Serie("imagen", "breaking bad", "Estrena todos los lunes")
serie1 = Serie("imagen", "game of thrones", "Estrena todos los jueves")
serie2 = Serie("imagen", "morty", "Estrena todos los juernes anashe")
cAtegoria = Categoria("Estreno semanal")
cAtegoria.agregar_serie(serie)
cAtegoria.agregar_serie(serie1)
cAtegoria.agregar_serie(serie2)
cAtegoria.imprimir()