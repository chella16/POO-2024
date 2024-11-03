from facade import Facade
# nose si deberia ser asi de sencillo
castor = "Castor"
cebolla = "Cebolla"
alpaca = "Alpaca"
carpincho = "Carpincho"
palindromo = "Palindromo"

traduccion = Facade.traduccion(castor)
min = Facade.minuscula(castor)
may = Facade.mayuscula (castor)

print (f"La palabra {castor} traducida: {traduccion}, minusculizada: {min}, mayusculizada: {may}")

traduccion = Facade.traduccion(cebolla)
min = Facade.minuscula(cebolla)
may = Facade.mayuscula (cebolla)

print (f"La palabra {cebolla} traducida: {traduccion}, minusculizada: {min}, mayusculizada: {may}")

traduccion = Facade.traduccion(alpaca)
min = Facade.minuscula(alpaca)
may = Facade.mayuscula (alpaca)

print (f"La palabra {alpaca} traducida: {traduccion}, minusculizada: {min}, mayusculizada: {may}")

traduccion = Facade.traduccion(carpincho)
min = Facade.minuscula(carpincho)
may = Facade.mayuscula (carpincho)

print (f"La palabra {carpincho} traducida: {traduccion}, minusculizada: {min}, mayusculizada: {may}")

traduccion = Facade.traduccion(palindromo)
min = Facade.minuscula(palindromo)
may = Facade.mayuscula (palindromo)

print (f"La palabra {palindromo} traducida: {traduccion}, minusculizada: {min}, mayusculizada: {may}")