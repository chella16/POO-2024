
class Personal():
    
    def __init__(self, nombre_empleado, antiguedad, sector) :
        self._nombre_completo = nombre_empleado
        self._antiguedad_empleado = antiguedad
        self._sector_empleado = sector
    
    def __str__(self) :
        return (f"Empleado  {self.__nombre_completo} Antiguedad: {self.__antiguedad_empleado} Sector {self.__sector_empleado}")