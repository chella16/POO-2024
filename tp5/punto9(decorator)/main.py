from Productos import Producto_Normal, Producto_Yankee, Producto_Argentino

producto = Producto_Normal(777.77777)
precio_normal = producto.get_precio()
print (f"Este es el precio normal del producto hecho string: {precio_normal}")

producto_yankee = Producto_Yankee(producto)
precio_yankee = producto_yankee.get_precio()
print (f"Este es el precio YANKEE del producto hecho str: {precio_yankee}")

producto_argentino = Producto_Argentino(producto)
precio_argento = producto_argentino.get_precio()
print (f"Este es el precio ARGENTO del producto hecho str: {precio_argento}")

producto_hibrido = Producto_Yankee(producto_argentino) # XD
precio_argento = producto_argentino.get_precio()
print (f"Este es el precio ARGENTO del producto hecho str: {precio_argento}")

