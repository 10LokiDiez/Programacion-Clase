"""
Cree una clase llamada Producto con:
- nombre
- precio

Implemente el método __add__ para que al sumar 
dos productos se obtenga la suma de sus
precios.
"""

class Producto:
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    
    def __add__(self, otro):
        return self.precio + otro.precio
    
producto1 = Producto("Raton", 25)
producto2 = Producto("Teclado", 30)
print(producto1 + producto2)
        
