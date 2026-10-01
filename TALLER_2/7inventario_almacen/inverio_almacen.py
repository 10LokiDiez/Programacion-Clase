"""
7. Inventario de almacén
- Crea una clase `Producto` con atributos: código, nombre, cantidad, precio y
categoría.
- Implemente un método que permita guardar el inventario en `almacen.txt`.
- Otro método que lea el archivo y muestre el valor total en stock de cada categoría.
"""
import os
class Producto:
    codigo = 0
    def __init__(self,nombre,cantidad,precio,categoria):
        Producto.codigo +=1
        self.codigo = Producto.codigo 
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria
        
    @classmethod
    def valor_total(cls):
        return cls.valortotal
        
    def guardar_almacen(self, path_file):
        with open(path_file, "a") as file:
            file.write(f"{self.codigo},{self.nombre},{self.cantidad},{self.precio},{self.categoria}\n")
        
    @staticmethod
    def leer_archivo_valor(path_file):
        totales_categoria = {}
        print("VALOR TOTAL EN STOCK")
        with open(path_file, "r") as file:
            text= file.read()
            for linea in text.split("\n"):
                if not linea:
                    continue
                codigo, nombre, cantidad, precio, categoria = linea.split(",")
                valor_stock = int(cantidad) * float(precio)

                # Acumula el valor según la categoría
                if categoria in totales_categoria:
                    totales_categoria[categoria] += valor_stock
                else:
                    totales_categoria[categoria] = valor_stock

        print("--- Valor Total en Stock por Categoria ---")
        for categoria, valor_total in totales_categoria.items():
            print(f"Categoria: {categoria:15} | Valor en Stock: ${valor_total:,.1f}")
                
        
        
def verificar_archivo(path_file):
    if os.path.exists(path_file):
        os.remove(path_file)
        
        
def main():
    
    path_file = os.path.join(os.path.dirname(__file__), "almacen.txt")
        
    lista_productos = [
        Producto("Arroz 1kg", 50, 4200.0, "Abarrotes"),
        Producto("Aceite Vegetal 1L", 30, 12500.0, "Abarrotes"),
        Producto("Detergente Liquido 2L", 20, 22000.0, "Aseo"),
        Producto("Jabon de Bano", 60, 3500.0, "Aseo"),
        Producto("Televisor Smart 43", 8, 1200000.0, "Electronica"),
        Producto("Audifonos Bluetooth", 15, 85000.0, "Electronica")
    ]
    verificar_archivo(path_file)
    
    for producto in lista_productos:
        producto.guardar_almacen(path_file)
    
    Producto.leer_archivo_valor(path_file)
        
        
if __name__ == '__main__':
    main()       