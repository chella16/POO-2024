#Python:¿Cómo debe ser compartida si trabajamos con
# Thread? ¿Y con Process?

#Si trababajamos con thread tenemos que usar una variable global
# y hacer referencia a ella en un proceso almacenado en una
#clase de tipo thread, creamos 4 objetos de esa clase y
# comenzamos cada uno de estos hilos y luego los joineamos
# Si trabajamos con multiprocessing tenemos que hacer una
#variable compartida en el main, la sitaxis de if name = main
# es obligatoria, cuando la creamos tenemos que indicar
#que tipo de variable es y su valor inicial y cuando
#referenciamos a ella en el proceso de incrementacion en
#la clase de process tenemos que indicar con el with getlock
#un bloqueo para evitar condiciones de carrera XD. Despues
#en el main cuando creamos el process tenemos que crear un
#objeto de tipo process que referencie al metodo incrementar
#de la clase process que creamos y le indicamos los
#argumentos del mismo proceso, esta todo en la sintaxis