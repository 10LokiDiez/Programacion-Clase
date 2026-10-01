"""
3. Cree una clase `InventarioProducto` que gestione un listado de productos (nombre,
precio, cantidad). Agregue métodos para añadir productos, calcular el valor total del
inventario y guardar todo en un archivo.
"""
import os

class InventarioProducto:
    def __init__(self):
        self.listado = []
    
    def guardarProducto(self,nombre,precio,cantidad):
        self.listado.append([nombre,precio,cantidad])
    
    def calcularValor(self):
        suma = 0
        for lista in self.listado:
            suma += lista[1] * lista[2]
        return suma
    
    def guardarArchivo(self,path_file):
        with open(path_file, "w", encoding="utf-8") as file:
            for lista in self.listado:
                file.write(f"Nombre: {lista[0]}, Precio: {lista[1]}, Cantidad: {lista[2]}\n")
        
    
def main():
    path_file = os.path.join(os.path.dirname(__file__), "inventario.txt")
    mi_inventario = InventarioProducto()
    mi_inventario.guardarProducto("Laptop", 1200.50, 5)
    mi_inventario.guardarProducto("Raton Inalámbrico", 25.00, 20)
    mi_inventario.guardarProducto("Teclado Mecánico", 85.00, 10)
    print(mi_inventario.listado)
    print(f"El valor total del inventario es: {mi_inventario.calcularValor()}")
    mi_inventario.guardarArchivo(path_file)
    
if __name__ == "__main__":
    main()