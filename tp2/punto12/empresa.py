
class Empresa:
    
    def __init__(self, nombre_empresa, direccion_empresa):
        self.__nombre_empresa = nombre_empresa
        self.__direccion_empresa = direccion_empresa
        self.__lista_empleados = []
        
    def get_nombre_empresa(self):
        return self.__nombre_empresa
    
    def set_nombre_empresa(self, nombre_empresa):
        self.__nombre_empresa = nombre_empresa
    
    def get_direccion_empresa(self):
        return self.__direccion_empresa
    
    def set_direccion_empresa(self, direccion_empresa):
        self.__direccion_empresa = direccion_empresa
    
    def get_lista_empleados(self):
        return self.__lista_empleados # raro segun el profe
    
    def agregar_empleado (self, empleado):
        self.__lista_empleados.append(empleado)
    
    def cantidad_empleados (self):
        canti = 0
        for i in self.__lista_empleados:
            canti += 1
        return canti
    
    def imprimir_info_empresa(self):
        print(f"La empresa {self.__nombre_empresa} ; de Direccion : {self.__direccion_empresa} Cuenta con la siguiente lista de empleados")
        for integrante in self.__lista_empleados:
            print (f"Empleado: {integrante.str_persona__()}")
    