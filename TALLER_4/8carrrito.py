"""

Cree una clase llamada CarritoCompras que tenga:
- productos (lista)

Implemente:
- __len__ → cantidad de productos
- __str__ → mostrar todos los productos del carrito.
"""

class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        
    def __len__(self):
        return len(self.productos)
    
    def __str__(self):
        cadena = ""
        for producto in self.productos:
            cadena = cadena + producto + " "
            
        return cadena
        
carrito1 = CarritoCompras()
carrito1.agregar_producto("Cuaderno")
carrito1.agregar_producto("Manzana")
carrito1.agregar_producto("Cereal")
carrito1.agregar_producto("Jabon")
carrito1.agregar_producto("Carne")
print(carrito1)
print(len(carrito1))