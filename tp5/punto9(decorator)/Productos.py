from abc import ABC
class Producto(ABC):
    def __init__(self, precio):
        self._precio = precio
    
    def get_precio (self):
        pass

class Producto_Normal (Producto):
    def __init__(self, precio):
        super().__init__(precio)
    
    def get_precio(self):
        precio = str(round(self._precio, 2))
        return precio

class Producto_Decorator (Producto):
    def __init__(self, producto: Producto):
        self._producto = producto
    
    def producto (self):
        return self._producto
    
    def get_precio(self):
        return self._producto.get_precio()
    
    def get_line_description (self):
        pass

class Producto_Yankee (Producto_Decorator):
    def get_line_description(self):
        return "$USD"
    
    def get_precio(self):
        precio = super().get_precio()
        signo = self.get_line_description()
        precio = signo + " " + precio
        return precio

class Producto_Argentino (Producto_Decorator):
    def get_line_description(self):
        return "$ARS"
    
    def get_precio(self):
        precio = super().get_precio()
        signo = self.get_line_description()
        precio = signo + " " + precio
        return precio